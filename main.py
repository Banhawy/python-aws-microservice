from fastapi import FastAPI
import uvicorn
from mylib.logic import (wiki, search_wiki)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/wiki/{name}")
async def wiki_name(name: str):
    """Get wikipedia definition for given name"""

    result = wiki(name)
    return {"message": result}

@app.get("/search/{value}")
async def search(value: str):
    """Page to search in Wikipedia"""

    results = search_wiki(value)
    return {"message": results}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')