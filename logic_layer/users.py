from logic_layer import data, user as u, song as s, connections as con
from infra_layer import connections


# add user to system
def add_user(user):
    return connections.add_user(user)


# return server response with data
def get_response_ok(input_data):
    obj = {'data': input_data,
           'message': 'OK'}
    return obj


# return server response for add_user
def get_res_add_user(user):
    return get_response_ok(user[data.user_name_field])


# get user from system
def get_user(user):
    return connections.get_user(user)


# return server response for get_user
def get_res_get_user(user):
    return get_response_ok(user)


# delete all users from system
def remove_all_users():
    return connections.delete_all_users()


# add friend to user
def add_friend(user):
    return connections.add_friend(user)


# return server response for add_user
def get_res_add_friend(friend):
    return get_response_ok(friend)


# change user password
def change_password(user):
    return connections.change_password(user)


# return server response for get_user
def get_res_change_password(user):
    return get_res_get_user(user)


# add playlist to user
def add_playlist(user):
    return connections.add_playlist(user)


# return server response for add_playlist
def get_res_add_playlist(playlist):
    return get_response_ok(playlist)


# return playlist from a server
def get_playlist(user):
    return connections.get_playlist(user)


# return server response for empty list
def get_res_empty_list():
    return get_response_ok([])


def get_response_fail(error):
    return {'error': error}


def get_fail_res_add_user(user):
    return get_response_fail('user with name ' + user[data.user_name_field] + ' already exists.')


def get_fail_res_add_friend():
    return get_response_fail('either the user name or the password are wrong')


# creating default user with default playlist and song in it as test prepare
def create_user_with_playlist_and_song(user_name=data.user_name, password='pass', playlist=data.password,
                                       song=None):
    if create_user_with_playlist(user_name, password, playlist):
        if song is None:
            song = s.Song()
        if 'error' not in connections.add_song(song.get_add_song_schema()):
            if 'error' not in con.add_song_to_playlist(user_name, password, playlist, song.get_title()):
                return True
    return False


# creating default user with default playlist as test prepare
def create_user_with_playlist(user_name=data.user_name, password='pass', playlist=data.password):
    user = u.User(user_name, password)
    if 'error' not in connections.add_user(user.get_user()):
        if 'error' not in connections.add_playlist(user.add_item(data.playlist_field, playlist)):
            return True
    return False
