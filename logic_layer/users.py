from infra_layer import connections


def add_user(user):
    return connections.add_user(user)


def get_user(user):
    return connections.get_user(user)


def remove_all_users():
    return connections.delete_all_users()

