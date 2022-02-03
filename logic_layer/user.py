import json


class User:
    # initialize user for test
    def __init__(self, name, password=None, friends=None, playlists=None):
        self.user = {'user_name': name}
        if password is None:
            self.user['user_password'] = 'pass'
        else:
            self.user['user_password'] = password
        if friends is None:
            self.user['friends'] = []
        else:
            self.user['friends'] = friends
        if playlists is None:
            self.user['playlists'] = []
        else:
            self.user['playlists'] = playlists

    # return user
    def get_user(self):
        return self.user

    # return user
    def get_user_for_print(self):
        new_user = self.user
        new_user.pop('user_password')
        return new_user

    # add friend
    def add_friend(self, friend):
        self.user['friends'].append(friend)
        return self.get_user()

    # return copy of user with new key\value pair
    def add_item(self, key, value):
        new_user = self.user.copy()
        new_user[key] = value
        return new_user
