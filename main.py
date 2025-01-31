from fastapi import FastAPI
from routes.routes import router

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


