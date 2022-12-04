from fastapi import FastAPI
import uvicorn
from mylib.routers import healthcheck, wiki

app = FastAPI()

app.include_router(healthcheck.router)
app.include_router(wiki.router)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')