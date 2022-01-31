import requests

"""
Class helps to connect to server by schemas
"""


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
    # timeout for connection
    timeout = 0.01

    # general connection with params schema and basic exception catch
    def get_request(self, request, err_msg='There was an error', params=None, option='GET'):
        try:
            if option == 'GET':
                req = requests.get(con.url + request, params=params, timeout=self.timeout)
            elif option == 'PUT':
                req = requests.put(con.url + request, json=params, timeout=self.timeout)
            elif option == 'POST':
                req = requests.post(con.url + request, json=params, timeout=self.timeout)
            if req.status_code == 200:
                return req.json()
            else:
                return err_msg + ' ' + str(req)
        except requests.ConnectionError:
            return 'There is no connection to the server'

    """
    return all user data by username
    {
        'user_name' : 'username'
    }
    """
    def get_user(self, params):
        return self.get_request(con.api['users']['get_user'], 'Something was wrong with getting user', params, 'GET')

    """
    return user playlist
    {
        'user_name': 'username',
        'user_password': 'password',
        'playlist_name': 'playlist_name'
    }
    """
    def get_playlist(self, params):
        return self.get_request(con.api['users']['get_playlist'], 'Something was wrong with getting playlist', params,
                                'GET')

    """
    add friend for user by friend name
    {
        'user_name': 'username',
        'user_password': 'password',
        'friend_name': 'friend_name'
    }
    """
    def add_friend(self, json):
        return self.get_request(con.api['users']['add_friend'], 'Something was wrong with adding friend', json, 'PUT')

    """
    change user password
    {
        'user_name': 'username',
        'user_password': 'password',
        'user_new_password': 'user_new_password'
    }
    """
    def change_password(self, json):
        return self.get_request(con.api['users']['change_password'], 'Something was wrong with changing password',
                                json, 'PUT')

    """
    add new user
    {
        'user_name': 'user_name',
        'user_password': 'user_password'
    }
    """
    def add_user(self, json):
        return self.get_request(con.api['users']['add_user'], 'Something was wrong with adding new user', json, 'POST')

    """
    add new playlist to user
    {
        'user_name': 'user_name',
        'user_password': 'user_password',
        'playlist_name: 'playlist_name'
    }
    """
    def add_playlist(self, json):
        return self.get_request(con.api['users']['add_playlist'], 'Something was wrong with adding new playlist',
                                json, 'POST')


con = APIConnections()
user = {
    "playlist_name": "my new playlist",
    "user_name": "Arnold",
    "user_password": "topsicret",
    "friend_name": 'Eytan',
    # 'user_new_password': 'topsicret'
}
new_user = {
    'user_name': 'Denys',
    'user_password': 'mypass'
}
new_playlist = {
    'user_name': 'Denys',
    'user_password': 'mypass'
}
print(con.get_user(user))
# print(con.get_playlist(user))
# req = requests.put(con.url + 'users/add_friend', json=user, timeout=0.1)
# print(con.add_friend(user))
# print(con.change_password(user))
# print(con.add_user(new_user))
# print(con.add_playlist(user))


