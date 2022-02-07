from infra_layer import connections


# call to api connect to server
def add_song_to_playlist(user='user', password='pass', playlist='playlist', song='song'):
    return connections.add_song_to_playlist({
        'playlist_name': playlist,
        'song_title': song,
        'user_name': user,
        'user_password': password
    })
