# user to add
user = {
    'user_name': 'user',
    'user_password': 'pass'
}

# user to get
get_user = {'data': {'friends': [], 'playlists': [], 'user_name': 'user'}, 'message': 'OK'}

# user to add friend
user_with_friend = {
    'user_name': 'friendly_user',
    'user_password': 'friend',
    'friend_name': 'best_friend'
}

# user to get after friend added
get_user_with_friend = {'data': {'friends': ['best_friend'], 'playlists': [], 'user_name': 'friendly_user'},
                        'message': 'OK'}

# user for password change test
user_with_pass = {
    'user_name': 'user_with_pass',
    'user_password': 'pass',
    'user_new_password': 'new_pass'
}

# user to get after password change
get_user_with_pass = {'data': {'friends': [], 'playlists': [], 'user_name': 'user_with_pass'}, 'message': 'OK'}

# user for adding playlist
user_with_playlist = {
    'user_name': 'user_with_playlist',
    'user_password': 'pass',
    'playlist_name': 'new_playlist'
}

# user to get after adding playlist
get_user_with_playlist = {'data': {'friends': [], 'playlists': ['new_playlist'], 'user_name': 'user_with_playlist'},
                          'message': 'OK'}

# song to add
song = {
    'song_genre': 'genre',
    'song_performer': 'performer',
    'song_title': 'title',
    'song_year': 1900
}

# song to get
get_song = {'data': {'genre': 'genre', 'performer': 'performer', 'rating': 0, 'title': 'title', 'year': '1900'},
            'message': 'OK'}
