from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
def create_app(database_path=None):
    app = FastAPI()
    @app.get('/api/health')
    def health(): return {'status':'ok'}
    app.mount('/', StaticFiles(directory=Path(__file__).parent/'static',html=True), name='static')
    return app
app=create_app()
