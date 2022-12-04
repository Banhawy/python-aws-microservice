from fastapi import APIRouter
from mylib.controllers.wiki import (wiki, search_wiki)

router = APIRouter(
    prefix="/wiki",
    tags=["wiki"],
    responses={404: {"description": "Not Found"}}
)

@router.get("/{name}")
async def wiki_name(name: str):
    """Get wikipedia definition for given name"""

    result = wiki(name)
    return {"message": result}

@router.get("/search/{value}")
async def search(value: str):
    """Page to search in Wikipedia"""

    results = search_wiki(value)
    return {"message": results}