from typing import Union

from fastapi import FastAPI

app = FastAPI()

ENVIRON = os.getenv("ENVIRON")

@app.get("/")
def read_root():
    return {"Hello": "World"}