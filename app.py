import falcon

from resources import user

api = application = falcon.API()

user_object = user.User()
user_collection = user.UserCollection()

api.add_route('/user', user_object)
api.add_route('/user/list', user_collection)
