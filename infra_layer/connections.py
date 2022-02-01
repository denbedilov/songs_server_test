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
        },
        'songs': {
            'add_song': 'songs/add_song',
            'down_vote': 'songs/downvote',
            'get_song': 'songs/get_song',
            'ranked_songs': 'songs/ranked_songs',
            'upvote': 'songs/upvote'
        },
        'playlists': {
            'add_song': 'playlists/add_song'
        },
        'admin': {
            'delete_all_songs': 'admin/delete_all_songs',
            'delete_all_users': 'admin/delete_all_users',
            'set_songs': 'admin/set_songs',
            'set_users': 'admin/set_users'
        }
    }

    # timeout for connection
    timeout = 0.01

    # general connection with params schema and basic exception catch
    def get_request(self, request, err_msg='There was an error', params=None, option='GET'):
        try:
            req = None
            if option == 'GET':
                req = requests.get(self.url + request, params=params, timeout=self.timeout)
            elif option == 'PUT':
                req = requests.put(self.url + request, json=params, timeout=self.timeout)
            elif option == 'POST':
                req = requests.post(self.url + request, json=params, timeout=self.timeout)
            elif option == 'DELETE':
                req = requests.delete(self.url + request, timeout=self.timeout)
            if req is not None and req.status_code == 200:
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
        return self.get_request(self.api['users']['get_user'], 'Something was wrong with getting user', params, 'GET')

    """
    return user playlist
    {
        'user_name': 'username',
        'user_password': 'password',
        'playlist_name': 'playlist_name'
    }
    """

    def get_playlist(self, params):
        return self.get_request(self.api['users']['get_playlist'], 'Something was wrong with getting playlist', params,
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
        return self.get_request(self.api['users']['add_friend'], 'Something was wrong with adding friend', json, 'PUT')

    """
    change user password
    {
        'user_name': 'username',
        'user_password': 'password',
        'user_new_password': 'user_new_password'
    }
    """

    def change_password(self, json):
        return self.get_request(self.api['users']['change_password'], 'Something was wrong with changing password',
                                json, 'PUT')

    """
    add new user
    {
        'user_name': 'user_name',
        'user_password': 'user_password'
    }
    """

    def add_user(self, json):
        return self.get_request(self.api['users']['add_user'], 'Something was wrong with adding new user', json, 'POST')

    """
    add new playlist to user
    {
        'user_name': 'user_name',
        'user_password': 'user_password',
        'playlist_name: 'playlist_name'
    }
    """

    def add_playlist(self, json):
        return self.get_request(self.api['users']['add_playlist'], 'Something was wrong with adding new playlist',
                                json, 'POST')

    """
    add song
    {
        'song_genre': 'song_genre',
        'song_performer': 'song_performer',
        'song_title': 'song_title',
        'song_year': 'song_year'
    }
    """

    def add_song(self, json):
        return self.get_request(self.api['songs']['add_song'], 'Something was wrong with adding new song',
                                json, 'POST')

    """
    down vote the song
    {
        'playlist_name': 'playlist_name',
        'song_title': 'song_title',
        'user_name': 'user_name',
        'user_password': 'user_password'
    }
    """

    def down_vote(self, json):
        return self.get_request(self.api['songs']['down_vote'], 'Something was wrong with down voting song',
                                json, 'PUT')

    """
    return song by its name
    {
        'song_title': 'song_title'
    }
    """

    def get_song(self, params):
        return self.get_request(self.api['songs']['get_song'], 'Something was wrong with getting song', params, 'GET')

    """
    return list of songs by its rating
    rating can be less, greater or equal to specified
    {
        'rank': 'rank',
        'op': 'less/eq/greater'
    }
    """

    def ranked_songs(self, params):
        return self.get_request(self.api['songs']['ranked_songs'], 'Something was wrong with getting ranked songs',
                                params, 'GET')

    """
    up vote the song
    {
        'playlist_name': 'playlist_name',
        'song_title': 'song_title',
        'user_name': 'user_name',
        'user_password': 'user_password'
    }
    """

    def up_vote(self, json):
        return self.get_request(self.api['songs']['upvote'], 'Something was wrong with up voting song',
                                json, 'PUT')

    """
    add song to playlist
    {
        'playlist_name': 'playlist_name',
        'song_title': 'song_title',
        'user_name': 'user_name',
        'user_password': 'user_password'
    }
    """

    def add_song_to_playlist(self, json):
        return self.get_request(self.api['playlists']['add_song'], 'Something was wrong with adding song to playlist',
                                json, 'POST')

    """
    delete all songs data
    """
    def delete_all_songs(self):
        return self.get_request(self.api['admin']['delete_all_songs'],
                                'Something was wrong with deleting all songs', None, 'DELETE')

    """
    delete all users data
    """
    def delete_all_users(self):
        return self.get_request(self.api['admin']['delete_all_users'],
                                'Something was wrong with deleting all users', None, 'DELETE')

    """
    upload array of users
    {   'users': {
            "user": {
                "password": "password",
                "name": "name",
                'friends': [],
                'playlists': {}
            },
            "user": {
                "password": "password",
                "name": "name",
                'friends': [],
                'playlists': {}
    }}
    """
    def set_users(self, json):
        return self.get_request(self.api['admin']['set_users'], 'Something was wrong with setting users', json, 'POST')

    """
    upload array of songs
    {
    'songs': [{
        "genre": "genre",
        "performer": "performer",
        "title": "title",
        "year": 0,
        "rating": 0},
        {
            "genre": "genre",
            "performer": "performer",
            "title": "title",
            "year": 0,
            "rating": 0}]}
    """
    def set_songs(self, json):
        return self.get_request(self.api['admin']['set_songs'], 'Something was wrong with setting songs', json, 'POST')
