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

    timeout = 0.01

    def get_request(self, request, err_msg='There was an error', params=None,):
        try:
            req = requests.get(con.url + request, params=params, timeout=self.timeout)
            if req.status_code == 200:
                return req.json()
            else:
                return err_msg
        except requests.ConnectionError:
            return 'There is no connection to the server'

    def get_user(self, user):
        return self.get_request(con.api['users']['get_user'], 'Something was wrong with getting user', user)

    def get_playlist(self, user):
        return self.get_request(con.api['users']['get_playlist'], 'Something was wrong with getting playlist', user)


con = APIConnections()
user = {
    'playlist_name': "myplaylist",
    'user_name': "Arnold",
    'user_password': "topsicret"
}
# print(con.get_user(user))
print(con.get_playlist(user))
