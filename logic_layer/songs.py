from infra_layer import connections


# delete all users from system
def remove_all_songs():
    return connections.delete_all_songs()


# add song to system
def add_song(song):
    return connections.add_song(song)


# return server response with data
def get_response_ok(input_data):
    return {'data': input_data,
            'message': 'OK'}


# return server response for add song
def get_res_add_song(song):
    return get_response_ok(song['title'])


# get song from system
def get_song(song):
    return connections.get_song(song)


# get server response for get song
def get_res_get_song(song):
    return get_response_ok(song)


# upvote song
def upvote(song):
    return connections.up_vote(song)


# get server response for up vote
def get_res_upvote(song):
    return get_response_ok(song)


# upvote song
def down_vote(song):
    return connections.down_vote(song)


# get server response for down vote
def get_res_down_vote(song):
    return get_response_ok(song)
