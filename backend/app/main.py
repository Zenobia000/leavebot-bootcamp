from contextlib import asynccontextmanager, contextmanager
from datetime import date
from pathlib import Path
import os, re, sqlite3
from fastapi import Body, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from .rules import leave_days

REASON_MAX=100
@contextmanager
def connect(path):
    c=sqlite3.connect(path);c.row_factory=sqlite3.Row;c.execute('PRAGMA foreign_keys=ON')
    try:
        yield c
        c.commit()
    except Exception:
        c.rollback();raise
    finally: c.close()

def create_app(database_path=None):
    path=Path(database_path or os.getenv('LEAVEBOT_DB','backend/data/leavebot.db'))
    @asynccontextmanager
    async def lifespan(app):
        path.parent.mkdir(parents=True,exist_ok=True)
        with connect(path) as c:
            c.executescript("""CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY,name TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS leaves(id INTEGER PRIMARY KEY,employee_id INTEGER NOT NULL REFERENCES employees(id),leave_type TEXT NOT NULL,start_date TEXT NOT NULL,end_date TEXT NOT NULL,period TEXT NOT NULL,reason TEXT NOT NULL,days REAL NOT NULL,status TEXT NOT NULL CHECK(status='pending'));""")
            c.executemany('INSERT OR IGNORE INTO employees VALUES(?,?)',[(1,'小安'),(2,'小晴')])
        yield
    app=FastAPI(lifespan=lifespan)
    @app.get('/api/health')
    def health(): return {'status':'ok'}
    @app.get('/api/employees')
    def employees():
        with connect(path) as c:return [dict(r) for r in c.execute('SELECT id,name FROM employees ORDER BY id')]
    @app.get('/api/leaves')
    def leaves(employee_id:int):
        with connect(path) as c:
            if not c.execute('SELECT id FROM employees WHERE id=?',(employee_id,)).fetchone():raise HTTPException(404,'找不到員工')
            return [dict(r) for r in c.execute('SELECT * FROM leaves WHERE employee_id=? ORDER BY id DESC',(employee_id,))]
    @app.post('/api/leaves',status_code=201)
    def submit(body:dict=Body(...)):
        required={'employee_id','leave_type','start_date','end_date','period'}
        if not required.issubset(body) or set(body)-required-{'reason'}:raise HTTPException(422,'欄位缺漏或含不允許欄位')
        if type(body['employee_id']) is not int or body['leave_type'] not in ['annual','personal','sick'] or body['period'] not in ['full','am','pm']:raise HTTPException(422,'員工、假別或時段不合法')
        reason=body.get('reason','')
        if not isinstance(reason,str) or len(reason)>REASON_MAX:raise HTTPException(422,f'理由最多{REASON_MAX}字')
        try:
            if any(not isinstance(body[k],str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',body[k]) for k in ['start_date','end_date']):raise ValueError('請使用YYYY-MM-DD日期')
            start=date.fromisoformat(body['start_date']);end=date.fromisoformat(body['end_date'])
            days=leave_days(start,end,body['period'])
        except ValueError as e:raise HTTPException(422,str(e)) from e
        with connect(path) as c:
            if not c.execute('SELECT id FROM employees WHERE id=?',(body['employee_id'],)).fetchone():raise HTTPException(422,'找不到員工')
            cur=c.execute('INSERT INTO leaves(employee_id,leave_type,start_date,end_date,period,reason,days,status) VALUES(?,?,?,?,?,?,?,?)',(body['employee_id'],body['leave_type'],body['start_date'],body['end_date'],body['period'],reason,days,'pending'))
            return dict(c.execute('SELECT * FROM leaves WHERE id=?',(cur.lastrowid,)).fetchone())
    app.mount('/',StaticFiles(directory=Path(__file__).parent/'static',html=True),name='static')
    return app
app=create_app()
