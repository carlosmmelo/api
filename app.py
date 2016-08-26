import falcon

from resources import user

api = application = falcon.API()

user_collection = user.UserCollection()

api.add_route('/user/list', user_collection)
# api.add_route('/user/{id}', user_collection)