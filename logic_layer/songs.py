from infra_layer import connections


# delete all users from system
def remove_all_songs():
    return connections.delete_all_songs()


# add song to system
def add_song(song):
    return connections.add_song(song)


# get song from system
def get_song(song):
    return connections.get_song(song)
