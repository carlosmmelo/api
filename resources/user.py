import falcon
from data_sources.postgres import Postgres
from resources import constant
import json
import datetime


class UserCollection(object):

    postgres_session = Postgres()

    def on_get(self, req, resp):
        user_list = Postgres.send_committed_query(self.postgres_session, constant.GET_ALL_USERS)
        json.JSONEncoder.default = lambda self, obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)
        resp.body = json.dumps({"message": "Get user list success", "users": user_list})
        resp.status = falcon.HTTP_200


class User(object):

    def on_get(self, req, resp):
        resp.body = '{"message": "Get user success"}'
        print(req.query_string)
        print(req.params)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        resp.body = '{"message" Create user success}'
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_204

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_204
