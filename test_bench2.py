#using pytest
#to run tests; install necessary libraries and pytest; run "pytest" 
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_put_sucsess_standard():
    response = client.post(
        "accounts/500",
        json={'name':'Test_name','description':'Test_description','balance':100.0,'active':True},
    )
    assert response.status_code == 201
    assert response.json() == {
        "name": "Test_name",
        "description": "Test_description",
        "balance": 100,
        "active": True,
    }

def test_put_fail_duplicate():
    response = client.post(
        "accounts/999",
        json={'name':'Test_name','description':'Test_description','balance':100.0,'active':True},
    )
    assert response.status_code == 409


def test_put_fail_string_id():
    response = client.post(
        "accounts/string",
        json={'name':'Test_name','description':'Test_description','balance':100.0,'active':True},
    )
    assert response.status_code == 422 #https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422

def test_put_fail_invalidname():
    response = client.post(
        "accounts/string",
        json={'name':True,'description':'Test_description','balance':100.0,'active':True},
    )
    assert response.status_code == 422 #https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422

def test_put_fail_invalid_description():
    response = client.post(
        "accounts/string",
        json={'name':"Test_name",'description':999,'balance':100.0,'active':True},
    )
    assert response.status_code == 422 #https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422

def test_put_fail_invalid_balance():
    response = client.post(
        "accounts/string",
        json={'name':"Test_name",'description':'Test_description','balance':'100.0','active':True},
    )
    assert response.status_code == 422 #https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422

def test_put_fail_invalid_active():
    response = client.post(
        "accounts/string",
        json={'name':"Test_name",'description':999,'balance':100.0,'active':"True"},
    )
    assert response.status_code == 422 #https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422

def test_put_sucsess_int_balance():
    response = client.post(
        "accounts/502",
        json={'name':'Test_name','description':'Test_description','balance':100,'active':True},
    )
    assert response.status_code == 201
    assert response.json() == {
        "name": "Test_name",
        "description": "Test_description",
        "balance": 100,
        "active": True,
    }

def test_healthz_sucsess():
    response = client.get(
        "/healthz",
    )
    assert response.status_code == 200
    assert response.json() == {
        "status": True,
    }

def test_get_sucsess_standard():
    response = client.get(
        "accounts/999",
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "Test_name1",
        "description": "Test_description1",
        "balance": 100,
        "active": False,
    }

def test_get_fail_no_exist():
    response = client.get(
        "accounts/1000",
    )
    assert response.status_code == 404

def test_get_string_ID():
    response = client.get(
        "accounts/string",
    )
    assert response.status_code == 422 #https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422