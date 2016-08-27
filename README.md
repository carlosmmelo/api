# api

prototype for API

We use `gnunicorn` for servicing the app:

```
gunicorn app
```

## Testing the initial User resource:

```
api git:(master) ✗ http localhost:8000/user/list
HTTP/1.1 200 OK
Connection: close
Date: Fri, 26 Aug 2016 22:01:29 GMT
Server: gunicorn/19.4.5
content-length: 36
content-type: application/json; charset=utf-8

{
    "message": "Get user list success"
}
```
```
(api) ➜  api git:(master) ✗ http POST localhost:8000/user/list
HTTP/1.1 201 Created
Connection: close
Date: Fri, 26 Aug 2016 22:01:40 GMT
Server: gunicorn/19.4.5
content-length: 31
content-type: application/json; charset=utf-8

{"message" Create user success}
```
```
(api) ➜  api git:(master) ✗ http PUT localhost:8000/user/list
HTTP/1.1 204 No Content
Connection: close
Date: Fri, 26 Aug 2016 22:02:00 GMT
Server: gunicorn/19.4.5
```
```
(api) ➜  api git:(master) ✗ http DELETE localhost:8000/user/list
HTTP/1.1 204 No Content
Connection: close
Date: Fri, 26 Aug 2016 22:03:48 GMT
Server: gunicorn/19.4.5
```
