import json
from logic_layer import data
from infra_layer import connections


# add user to system
def add_user(user):
    return connections.add_user(user)


# return server response for add_user
def get_res_add_user(user):
    return data.res_ok_head + user["user_name"] + data.res_ok_bot


# get user from system
def get_user(user):
    return connections.get_user(user)


# return server response for get_user
def get_res_get_user(user):
    return data.res_ok_head + json.dump(user, sort_keys=True) + data.res_ok_bot


# delete all users from system
def remove_all_users():
    return connections.delete_all_users()


# add friend to user
def add_friend(user):
    return connections.add_friend(user)


# return server response for add_user
def get_res_add_friend(friend):
    return data.res_ok_head + friend + data.res_ok_bot


# change user password
def change_password(user):
    return connections.change_password(user)
