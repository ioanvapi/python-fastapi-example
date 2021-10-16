from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
def index():
    return {"Hello", "World"}


@app.get("/task/{taskId}")
def getTask(taskId: int):
    return {"taskId": taskId}


@app.get("/item/{itemId}")
def getItem(itemId: int, qp: Optional[str] = None):
    return {"taskId": itemId, "qp": qp}
