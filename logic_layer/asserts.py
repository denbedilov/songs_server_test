from logic_layer import data, users, songs, playlists

# file for all assert functions


def add_user(user, fail=False):
    if not fail:
        return users.add_user(user.get_user()) == \
               users.get_res_add_user(user.get_user())
    else:
        return 'error' in users.add_user(user.get_user())


def get_user(user):
    return users.get_user(user.get_user()) == \
           users.get_res_get_user(user.get_user_for_print())


def add_friend(user, friend_name, fail=False):
    if not fail:
        return users.add_friend(user.add_friend(friend_name)) == \
               users.get_res_add_friend(friend_name)
    else:
        return 'error' in users.add_friend(user.add_friend(friend_name))


def get_friend(user):
    return users.get_user(user.get_user()) == \
           users.get_res_get_user(user.get_user_for_print())


def change_password(user, password, fail=False):
    if not fail:
        return users.change_password(user.add_item(data.password_field, password)) == \
               users.get_res_change_password(user.get_user_for_print())
    else:
        return 'error' in users.change_password(user.add_item(data.password_field, password))


def add_playlist(user, playlist, fail=False):
    if not fail:
        return users.add_playlist(user.add_item(data.playlist_field, playlist)) == \
               users.get_res_add_playlist(playlist)
    else:
        return 'error' in users.add_playlist(user.add_item(data.playlist_field, playlist))


def get_playlist(user, fail=False):
    if not fail:
        return users.get_playlist(user.add_item(data.playlist_field, data.playlist)) == \
               users.get_res_empty_list()
    else:
        return 'error' in users.get_playlist(user.add_item(data.playlist_field, data.playlist))


def add_song(song):
    return songs.add_song(song.get_add_song_schema()) == \
           songs.get_res_add_song(song.get_song())


def get_song(song):
    return songs.get_song(song.get_get_song_schema()) == \
           songs.get_res_get_song(song.get_song())


def upvote_song(song, user, playlist, fail=False):
    if not fail:
        return songs.upvote(song.get_upvote_schema(user, playlist)) == songs.get_res_upvote(song.get_rating())
    else:
        return 'error' in songs.upvote(song.get_upvote_schema(user, playlist))


def down_vote_song(song, user, playlist, fail=False):
    if not fail:
        return songs.down_vote(song.get_down_vote_schema(user, playlist)) == songs.get_res_down_vote(song.get_rating())
    else:
        return 'error' in songs.down_vote(song.get_down_vote_schema(user, playlist))


def ranked_songs(songs_arr, rating, operator):
    return songs.ranked_songs(rating, operator) == songs.get_res_ranked_songs(songs_arr, rating, operator)


def add_song_to_playlist(user, playlist_name, song_title, fail=False):
    if not fail:
        return playlists.add_song(user, playlist_name, song_title) == playlists.get_res_add_song(song_title)
    else:
        return 'error' in playlists.add_song(user, playlist_name, song_title)
