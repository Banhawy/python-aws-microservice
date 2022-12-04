from fastapi.testclient import TestClient
from main import app
from mylib.logic import wiki, search_wiki

client = TestClient(app)

def test_wiki():
    assert "god" in wiki()
    assert "Barack" in wiki(name="barak")

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_wiki_main():
    result = wiki("god")
    response = client.get("/wiki/god")
    assert response.status_code == 200
    assert response.json() == {"message": result}

def test_wiki_search():
    result = search_wiki("god")
    response = client.get("/search/god")
    assert response.status_code == 200
    assert response.json() == {"message": result}