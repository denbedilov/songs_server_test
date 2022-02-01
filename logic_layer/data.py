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
