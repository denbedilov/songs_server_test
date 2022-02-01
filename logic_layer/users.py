from infra_layer import connections


# add user to system
def add_user(user):
    return connections.add_user(user)


# get user from system
def get_user(user):
    return connections.get_user(user)


# delete all users from system
def remove_all_users():
    return connections.delete_all_users()


# add friend to user
def add_friend(user):
    return connections.add_friend(user)


# change user password
def change_password(user):
    return connections.change_password(user)
