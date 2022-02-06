from logic_layer import data
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
