from logic_layer import data, users

# file for all assert functions


def add_user(user):
    return users.add_user(user.get_user()) == \
           users.get_res_add_user(user.get_user())


def get_user(user):
    return users.get_user(user.get_user()) == \
           users.get_res_get_user(user.get_user_for_print())


def add_friend(user):
    return users.add_friend(user.add_item(data.friend_field, data.friend_name)) == \
           users.get_res_add_friend(data.friend_name)


def get_friend(user):
    return users.get_user(user.add_friend(data.friend_name)) == \
           users.get_res_get_user(user.get_user_for_print())


def change_password(user):
    return users.change_password(user.add_item(data.password_field, data.password)) == \
           users.get_res_change_password(user.get_user_for_print())


def add_playlist(user):
    return users.add_playlist(user.add_item(data.playlist_field, data.playlist)) == \
           users.get_res_add_playlist(data.playlist)


def get_playlist(user):
    return users.get_playlist(user.add_item(data.playlist_field, data.playlist)) == \
           users.get_res_empty_list()
