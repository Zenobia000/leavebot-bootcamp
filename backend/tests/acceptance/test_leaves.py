import pytest
from fastapi.testclient import TestClient
from app.main import create_app
@pytest.fixture
def client(tmp_path):
    with TestClient(create_app(tmp_path/'test.db')) as c: yield c
def valid(**updates):
    data=dict(employee_id=1,leave_type='annual',start_date='2026-10-20',end_date='2026-10-20',period='full',reason='休息一天')
    data.update(updates);return data
@pytest.mark.req('TC-01','AC-01.1','FR-01')
def test_submit_valid_leave_is_pending(client):
    r=client.post('/api/leaves',json=valid())
    assert r.status_code==201
    assert r.json()['status']=='pending'
    assert r.json()['days']==1
