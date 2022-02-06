from infra_layer import connections


# add song to playlist
def add_song(user, playlist_name, song_title):
    schema = user.get_user()
    schema['playlist_name'] = playlist_name
    schema['song_title'] = song_title
    return connections.add_song_to_playlist(schema)


# get server response for add song
def get_res_add_song(song_title):
    return get_response_ok(song_title)


# return server response with data
def get_response_ok(input_data):
    return {'data': input_data,
            'message': 'OK'}
