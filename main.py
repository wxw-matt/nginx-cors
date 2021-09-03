from typing import Optional

from fastapi import FastAPI

app = FastAPI()

access={}
access_cors={}


@app.get("/")
def get():
    global access
    if 'get' in access:
        del access['get']
        0 / 0
    access['get'] = True
    return {"Hello": "GET"}

@app.post("/")
def post():
    global access
    if 'post' in access:
        del access['post']
        0 / 0
    access['post'] = True
    return {"Hello": "POST"}

@app.put("/")
def put():
    global access
    if 'put' in access:
        del access['put']
        0 / 0
    access['put'] = True
    return {"Hello": "PUT"}

@app.delete("/")
def delete():
    global access
    if 'delete' in access:
        del access['delete']
        0 / 0
    access['delete'] = True
    return {"Hello": "DELETE"}

@app.head("/")
def head():
    global access
    if 'head' in access:
        del access['head']
        0 / 0
    access['head'] = True
    return {"Hello": "HEAD"}


###################
@app.get("/cors")
def cors_get():
    global access_cors
    if 'get' in access_cors:
        del access_cors['get']
        0 / 0
    access_cors['get'] = True
    return {"Hello cors": "GET"}

@app.post("/cors")
def cors_post():
    global access_cors
    if 'post' in access_cors:
        del access_cors['post']
        0 / 0
    access_cors['post'] = True
    return {"Hello cors": "POST"}

@app.put("/cors")
def cors_put():
    global access_cors
    if 'put' in access_cors:
        del access_cors['put']
        0 / 0
    access_cors['put'] = True
    return {"Hello cors": "PUT"}

@app.delete("/cors")
def cors_delete():
    global access_cors
    if 'delete' in access_cors:
        del access_cors['delete']
        0 / 0
    access_cors['delete'] = True
    return {"Hello cors": "DELETE"}

@app.head("/cors")
def cors_head():
    global access_cors
    if 'head' in access_cors:
        del access_cors['head']
        0 / 0
    access_cors['head'] = True
    return {"Hello cors": "HEAD"}