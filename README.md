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

## Testing Get All Users using DB

```
(api) ➜  api git:(master) ✗ http localhost:8000/user/list
HTTP/1.1 200 OK
Connection: close
Date: Sun, 28 Aug 2016 06:05:42 GMT
Server: gunicorn/19.4.5
content-length: 498
content-type: application/json; charset=utf-8

{
    "message": "Get user list success",
    "users": [
                {
                    'email': 'test@gmail.com',
                    'lastname': 'test1',
                    'isadmin': False,
                    'datecreated': datetime.datetime(2016, 8, 27, 14, 4, 40, 415385),
                    'id': 1,
                    'datemodified': datetime.datetime(2011, 5, 16, 15, 36, 38),
                    'firstname': 'test'
                }, 
                {
                    'email': 'test2@gmail.com',
                    'lastname': 'test2',
                    'isadmin': False,
                    'datecreated': datetime.datetime(2016, 8, 28, 1, 43, 52, 880591),
                    'id': 2,
                    'datemodified': datetime.datetime(2016, 8, 28, 2, 36, 38),
                    'firstname': 'test2'
                }
             ]
}
```

## Sample adding a new user to the User table

```
INSERT INTO Users (firstname, lastname, isadmin, email, datemodified)
    VALUES ('test2', 'test2', False, 'test2@gmail.com', TIMESTAMP '2016-08-28 02:36:38');
```

<!DOCTYPE html>
<html>
<head>
  <title></title>
</head>
<body>
<table border="1" style="border-collapse:collapse">
<tr><th>id</th><th>firstname</th><th>lastname</th><th>isadmin</th><th>email</th><th>datecreated</th><th>datemodified</th></tr>
<tr><td>1</td><td>test</td><td>test1</td><td>false</td><td>test@gmail.com</td><td>2016-08-27 14:04:40.415385</td><td>2011-05-16 15:36:38.000000</td></tr>
<tr><td>2</td><td>test2</td><td>test2</td><td>false</td><td>test2@gmail.com</td><td>2016-08-28 01:43:52.880591</td><td>2016-08-28 02:36:38.000000</td></tr></table>
</body>
</html>

Please refer to the DDL for new updates