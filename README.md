# How to using nginx-cors


## Start Docker containers
```bash
git clone https://github.com/wxw-matt/nginx-cors.git nginx-cors

cd nginx-cors
docker-compose up
```
`docker-compose up` starts two containers, one is a FastAPI server,
  another is a nginx server. The nginx server has been settled for nginx cors.
  It exposes `60000` port to host.
## Host configuration

  The only job for the host is to have a config file to make the port `60000` public.
  You can see `cors.conf` as an example.

  A quick command to enable this config file for nginx
  ```bash
  sudo ln -sfn cors.conf /etc/nginx/sites-enabled
  ```

## How to use it
  I use this website

  http://resttesttest.com/

## Get real client ip
  As we have two nginx, the FastAPI server cannot get the real client IP through
  `request.client.host`. Therefore, we need to add headers to the request in nginx config file.
  It looks like:
  ```
        proxy_set_header   X-Forwarded-For    $proxy_add_x_forwarded_for;
        proxy_set_header   X-Real-IP          $remote_addr;

  ```
  With that, the FastAPI headers should have two more items:`x-forwarded-for` and `x-real-ip`:
  ```json
  {
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
  ```
  The real ip can be simply retrieved by `request.headers["x-real-ip"]`.
