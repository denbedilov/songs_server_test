from logic_layer import data


class User:
    user_name_field = 'user_name'
    password_field = 'user_password'
    default_password = 'pass'
    friends_field = 'friends'
    playlists_field = 'playlists'

    # initialize user for test
    def __init__(self, name, password=None, friends=None, playlists=None):
        self.user = {self.user_name_field: name}
        if password is None:
            self.user[self.password_field] = self.default_password
        else:
            self.user[self.password_field] = password
        if friends is None:
            self.user[self.friends_field] = []
        else:
            self.user[self.friends_field] = friends
        if playlists is None:
            self.user[self.playlists_field] = []
        else:
            self.user[self.playlists_field] = playlists

    # return user
    def get_user(self):
        return {
            self.user_name_field: self.user[self.user_name_field],
            self.password_field: self.user[self.password_field]
        }

    # return user
    def get_user_for_print(self):
        new_user = self.user.copy()
        new_user.pop(self.password_field)
        return new_user

    # add friend
    def add_friend(self, friend_name):
        self.user[self.friends_field].append(friend_name)
        res_user = self.get_user()
        res_user[data.friend_field] = friend_name
        return res_user

    # return copy of user with new key\value pair
    def add_item(self, key, value):
        new_user = self.get_user()
        new_user[key] = value
        return new_user
