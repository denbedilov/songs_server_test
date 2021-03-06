# response OK header
res_ok_head = "{'data': '"

# response OK bottom
res_ok_bot = "', 'message': 'OK'}"

# test username
user_name = 'user'
user_name_field = 'user_name'

# output for test failed
assert_add_user = 'Add user not matched'

# output for test failed
assert_get_user = 'Get user not matched'

# friend name to add friend
friend_name = 'friend'
friend_name2 = 'friend 2'
friend_field = 'friend_name'

# output for test failed
assert_add_friend = 'Add friend not matched'

# output for test failed
assert_get_friend = 'Get friend not matched'

# password for change
password_field = 'user_new_password'
password = 'new_pass'

# output for test failed
assert_change_password = 'Change Password not matched'

# playlist to add
playlist_field = 'playlist_name'
playlist = 'playlist'
playlist2 = 'playlist 2'

# output for test failed
assert_add_playlist = 'Add playlist not matched'

# output for test failed
assert_get_playlist = 'Get playlist not matched'

# output for test failed
assert_add_song = 'Add song not matched'

# output for test failed
assert_get_song = 'Get song not matched'

# output for test failed
assert_upvote_song = 'Upvote not matched'

# output for test failed
assert_down_vote_song = 'Down vote not matched'

# output for test failed
assert_ranked_songs_less = 'Ranked songs less not matched'

# output for test failed
assert_ranked_songs_eq = 'Ranked songs eq not matched'

# output for test failed
assert_ranked_songs_greater = 'Ranked songs greater not matched'

# three different rating songs to set
three_dif_rating_songs = {
    'songs': [{
        "genre": "genre",
        "performer": "performer",
        "title": "song 1",
        "year": 0,
        "rating": 1},
        {
            "genre": "genre",
            "performer": "performer",
            "title": "song 2",
            "year": 0,
            "rating": 5},
        {
            "genre": "genre",
            "performer": "performer",
            "title": "song 3",
            "year": 0,
            "rating": 9}]}

# operators for ranked songs
rank_operators = ('less', 'eq', 'greater')

# output for test failed
assert_add_song_to_playlist = 'Add song to playlist not matched'

# output for test failed
assert_double_user = 'Add same user error not matched'

# output for test failed
assert_prepare_test = 'Prepare to test failed'

# default song title
default_song = 'song'

# output for test does not exist
assert_test_does_not_exist = 'Test does not exist'
