import falcon
from data_sources.postgres import Postgres
from resources import constant
import json
import datetime

postgres_session = Postgres()
json.JSONEncoder.default = lambda self, obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)


class UserCollection(object):

    def on_get(self, req, resp):
        user_list = Postgres.send_committed_query(postgres_session, constant.GET_ALL_USERS)
        resp.body = json.dumps({"message": "Get user list success", "users": user_list})
        resp.status = falcon.HTTP_200


class User(object):

    def on_get(self, req, resp):
        if not req.params:
            raise falcon.HTTPMissingParam('name or email')
        for param in req.params:
            if param not in ['firstname', 'lastname', 'email']:
                raise falcon.HTTPInvalidParam('Please use name or email as parameter', param)
            else:
                user_search = Postgres.send_committed_query(postgres_session, constant.SEARCH_USER.format(param=param, val=req.params[param]))
                resp.body = json.dumps({"message": "Search for user success", "users": user_search})
                resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        resp.body = '{"message" Create user success}'
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_204

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_204
