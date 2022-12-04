from fastapi.testclient import TestClient
from main import app
from mylib.controllers.wiki import wiki, search_wiki

client = TestClient(app)

def test_wiki():
    assert "god" in wiki()
    assert "Barack" in wiki(name="barak")

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_healthcheck():
    result = wiki("god")
    ping_response = client.get("/healthcheck/ping")
    ready_response = client.get("/healthcheck/ready")
    assert ping_response.status_code == 200
    assert ping_response.json() == "ok"
    assert ready_response.status_code == 200
    assert ready_response.json() == "ready"

def test_wiki_main():
    result = wiki("god")
    response = client.get("/wiki/god")
    assert response.status_code == 200
    assert response.json() == {"message": result}

def test_wiki_search():
    result = search_wiki("god")
    response = client.get("/wiki/search/god")
    assert response.status_code == 200
    assert response.json() == {"message": result}