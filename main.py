from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    isOffer: Optional[bool] = None # it is not required in a PUT

@app.get("/")
def index():
    return {"Hello", "World"}


@app.get("/task/{taskId}")
def getTask(taskId: int):
    return {"taskId": taskId}


@app.get("/item/{itemId}")
def getItem(itemId: int, qp: Optional[str] = None):
    return {"taskId": itemId, "qp": qp}


# creates a new item
@app.post("/item")
def newItem(item: Item):
    return {"item": item, "message": "New item created."}

# updates an item
@app.put("/item/{itemId}")
def updateItem(itemId: int, item: Item):
    return {"itemName": item.name, "itemPrice": item.price, "itemId": itemId}

    