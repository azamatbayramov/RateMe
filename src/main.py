from src.database import Base, engine
from fastapi import FastAPI

Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
