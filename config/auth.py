''' Where authentication settings should be'''
from app.Users import Users

'''
|--------------------------------------------------------------------------
| Authentication Model
|--------------------------------------------------------------------------
|
| Put the model here that will be used to authenticate users to your site.
| Currently the model must contain a password field. In the model should
| be an auth_column = 'column' in the Meta class. This column will be
| used to verify credentials in the Auth facade or any other auth
| classes. The auth_column will be used to change auth things
| like 'email' to 'user' to easily switch which column will
| be authenticated.
|
| @see packages.facades.Auth
|
'''

AUTH = {
    'model': Users,
    'driver': 'cookie'
}
