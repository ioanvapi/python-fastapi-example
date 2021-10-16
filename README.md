# Python FastAPI example

Simple web app written in Python. It uses FastAPI to create endpoints and is running using uvicorn.

* [FastAPI](https://github.com/tiangolo/fastapi)
* [uvicorn](https://www.uvicorn.org/)

## Prerequisites

I guess it's better to write every python app in its own virtual environment. Most of these libraries requires Python 3.6+.

``` bash
$ sudo apt install python3.8-venv
$ pip install --user virtualenv

# creates venv folder and its binary content
$ python -m venv venv

# activate venv
$ source venv/bin/activate

# or (in dev) install manually each library
$ pip install -r requirements.txt

$ pip install fastapi uvicorn
```

## Required libraries

* FastAPI (pip install fastapi)
* uvicorn
* 

## Start the server 

Start the server in reload mode. Each change in main.py file will be reloaded.


* main - comes from main.py 
* app - name of fastapi variable declared in main.py
  
``` bash
$ uvicorn main:app --reload

# It should display 
# Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Code

Update .gitignore with venv before commit.

### Add code to handle GET requests

Code below creates several endpoints, all for GET method request:

* / - handled by index() function
* /task/{taskId} - handled by getTask(taskId: int) that receives the **path param** from request. Test it with http://localhost:8000/task/25
* /item/{itemId} - handled by getItem(itemId: int, qp: Optional[str] = None) that receives both **path param** and **query param**. Test it with http://localhost:8000/item/12?qp=blue
  
**Note**: FastAPI provides usefull endpoints (swagger) to test this endpoints. You can use any of:
* [http://localhost:8000/docs](http://localhost:8000/docs)
* [http://localhost:8000/redoc](http://localhost:8000/redoc)


``` python
@app.get("/")
def index():
    return {"Hello", "World"}


@app.get("/task/{taskId}")
def getTask(taskId: int):
    return {"taskId": taskId}


@app.get("/item/{itemId}")
def getItem(itemId: int, qp: Optional[str] = None):
    return {"taskId": itemId, "qp": qp}

```

### Add code to handle POST and PUT requests 

It uses [pydantic](https://pydantic-docs.helpmanual.io/) for data validation, settings management and enforces type hints, user friedly error.

``` python
class Item(BaseModel):
    name: str
    price: float
    isOffer: Optional[bool] = None # it is not required in a POST/PUT

# creates a new item
@app.post("/item")
def newItem(item: Item):
    return {"item": item, "message": "New item created."}

# updates an item
@app.put("/item/{itemId}")
def updateItem(itemId: int, item: Item):
    return {"itemName": item.name, "itemPrice": item.price, "itemId": itemId}
```


### Enable CORS

FastAPI manages [CORS](https://fastapi.tiangolo.com/tutorial/cors/) by integrating a [middleware](https://fastapi.tiangolo.com/advanced/middleware/).

``` python
from fastapi.middleware.cors import CORSMiddleware

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
    allow_methods=["*"],
    allow_headers=["*"],
)
```






## Dockerize

[Here](https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-for-fastapi) is the way FastAPI recommend dockerizing the app.

