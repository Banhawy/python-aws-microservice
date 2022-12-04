from fastapi import APIRouter

router = APIRouter(
    prefix="/healthcheck",
    tags=["healthcheck"],
    responses={404: {"description": "Not Found"}}
)

@router.get("/ping")
async def wiki_name():
    """Ping the service"""

    return "ok"

@router.get("/ready")
async def search():
    """Check if service is ready"""

    return "ready"