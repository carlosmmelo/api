import falcon


class UserCollection(object):

    def on_get(self, req, resp):
        resp.body = '{"message": "Get user list success"}'
        resp.status = falcon.HTTP_200


class User(object):

    def on_get(self, req, resp):
        resp.body = '{"message": "Get user list success"}'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        resp.body = '{"message" Create user success}'
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_204

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_204
