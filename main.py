from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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


origins = [
    "http://localhost.com",
    "https://localhost.com",
    "http://localhost",
    "http://localhost:8080",
]

# The middleware will handle OPTIONS request with Origin and Access-Control-Request-Method headers
# but will pass the requests through as normal otherwise.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT"],
    allow_headers=["*"],
    max_age=3600,
)

