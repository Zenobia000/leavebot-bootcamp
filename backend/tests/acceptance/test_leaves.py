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

def count(client):return len(client.get('/api/leaves?employee_id=1').json())
@pytest.mark.req('TC-02','AC-01.2','FR-02')
def test_required_field_rejected_without_save(client):
    d=valid();d.pop('leave_type');before=count(client)
    assert client.post('/api/leaves',json=d).status_code==422
    assert count(client)==before
@pytest.mark.req('TC-03','AC-01.2','FR-02')
def test_reverse_date_rejected_without_save(client):
    assert client.post('/api/leaves',json=valid(end_date='2026-10-19')).status_code==422
    assert count(client)==0
@pytest.mark.req('TC-05','AC-01.4','FR-04')
def test_long_reason_rejected_without_save(client):
    assert client.post('/api/leaves',json=valid(reason='字'*201)).status_code==422
    assert count(client)==0
@pytest.mark.req('TC-06','AC-01.5','FR-05')
@pytest.mark.parametrize('extra',[{'status':'approved'},{'days':99}])
def test_client_cannot_set_trusted_values(client,extra):
    assert client.post('/api/leaves',json=valid(**extra)).status_code==422
    assert count(client)==0
@pytest.mark.req('TC-07','AC-02.1','FR-06')
def test_employees_do_not_mix(client):
    client.post('/api/leaves',json=valid())
    assert len(client.get('/api/leaves?employee_id=1').json())==1
    assert client.get('/api/leaves?employee_id=2').json()==[]
@pytest.mark.req('TC-07','AC-02.1','FR-06')
def test_data_persists_across_app_restart(tmp_path):
    path=tmp_path/'persist.db'
    with TestClient(create_app(path)) as c:assert c.post('/api/leaves',json=valid()).status_code==201
    with TestClient(create_app(path)) as c:assert len(c.get('/api/leaves?employee_id=1').json())==1
@pytest.mark.req('TC-08','AC-01.2','FR-02')
@pytest.mark.parametrize('changes',[{'employee_id':99},{'leave_type':'unknown'},{'period':'unknown'},{'start_date':'bad'}])
def test_invalid_values_do_not_save(client,changes):
    assert client.post('/api/leaves',json=valid(**changes)).status_code==422
    assert count(client)==0
