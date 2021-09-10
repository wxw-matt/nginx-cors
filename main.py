from typing import Optional

from fastapi import FastAPI, Request

app = FastAPI()

access={}
access_cors={}

"""
        proxy_set_header   Host               $host;
        proxy_set_header   X-Forwarded-For    $proxy_add_x_forwarded_for;
        proxy_set_header   X-Real-IP          $remote_addr;
        proxy_set_header   X-Forwarded-Proto  $scheme;
{
  "Hello": "GET",
  "IP": "172.19.0.3",
  "headers": {
    "x-forwarded-for": "27.33.198.223, 172.19.0.1",
    "host": "nginx.myminda.com",
    "connection": "close",
    "x-real-ip": "27.33.198.223",
    "x-forwarded-proto": "http",
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "http://resttesttest.com",
    "referer": "http://resttesttest.com/",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6"
  }
}
"""

@app.get("/")
def get(request: Request):
    global access
    client_host = request.client.host
    if 'get' in access:
        del access['get']
        0 / 0
    access['get'] = True
    return {"Hello": "GET", "IP": client_host, "real ip": request.headers["x-real-ip"], "headers" : request.headers}

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

@app.post("/myhook")
async def post(request: Request):
    print("myhook:")
    print(await request.json())
    return {"Hello": "POST"}
