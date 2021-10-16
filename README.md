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



