import requests


class APIConnections:
    url = "http://127.0.0.1:3002/"
    api = {
        'users': {
            'add_friend': 'users/add_friend',
            'add_playlist': 'users/add_playlist',
            'add_user': 'users/add_user',
            'change_password': 'users/change_password',
            'get_playlist': 'users/get_playlist',
            'get_user': 'users/get_user'
        }
    }
    params = {
        'get_user': '?user_name='
    }
    timeout = 0.01

    def get_user(self, username):
        try:
            req = requests.get(con.url + con.api['users']['get_user'] + con.params['get_user'] + username,
                               timeout=self.timeout)
            if req.status_code == 200:
                return req.json()
            else:
                return 'Something was wrong with getting user'
        except requests.ConnectionError:
            return 'There is no connection to the server'


con = APIConnections()
user = 'Arnold'
print(con.get_user(user))
