import pytest
from logic_layer import asserts, data, songs, users
from logic_layer.song import Song
from logic_layer.user import User


@pytest.mark.basic
@pytest.mark.songs
def test_add_song(remove_songs):
    s = Song()
    assert asserts.add_song(s), data.assert_add_song
    assert asserts.get_song(s), data.assert_get_song


@pytest.mark.basic
@pytest.mark.songs
def test_get_song(remove_songs):
    s = Song()
    assert asserts.add_song(s), data.assert_add_song
    assert asserts.get_song(s), data.assert_get_song


@pytest.mark.basic
@pytest.mark.songs
def test_upvote(remove_songs):
    u = User('user')
    s = Song()
    playlist = 'playlist'
    assert asserts.add_song(s), data.assert_add_song
    assert asserts.upvote_song(s, u, playlist), data.assert_upvote_song
    assert asserts.get_song(s), data.assert_get_song


@pytest.mark.basic
@pytest.mark.songs
def test_down_vote(remove_songs):
    u = User('user')
    s = Song()
    playlist = 'playlist'
    assert asserts.add_song(s), data.assert_add_song
    assert asserts.upvote_song(s, u, playlist), data.assert_upvote_song
    assert asserts.down_vote_song(s, u, playlist), data.assert_down_vote_song
    assert asserts.get_song(s), data.assert_get_song


@pytest.mark.basic
@pytest.mark.songs
def test_ranked_songs(remove_songs):
    # add three different rating songs
    songs_arr = songs.set_songs(data.three_dif_rating_songs)
    if songs_arr is not None:
        assert asserts.ranked_songs(songs_arr, songs_arr[0]['rating']+1, 'less'), data.assert_ranked_songs_less
        assert asserts.ranked_songs(songs_arr, songs_arr[1]['rating'], 'eq'), data.assert_ranked_songs_eq
        assert asserts.ranked_songs(songs_arr, songs_arr[2]['rating']-1, 'greater'), data.assert_ranked_songs_greater


@pytest.mark.xfail
@pytest.mark.songs
@pytest.mark.sys_req
def test_upvote_without_song():
    assert False, data.assert_test_does_not_exist


@pytest.mark.xfail
@pytest.mark.songs
@pytest.mark.sys_req
def test_down_vote_without_song():
    assert False, data.assert_test_does_not_exist


@pytest.mark.xfail
@pytest.mark.songs
@pytest.mark.sys_req
def test_get_song_without_song():
    assert False, data.assert_test_does_not_exist


@pytest.mark.songs
@pytest.mark.sys_req
def test_rank_less_zero(remove_songs, remove_users):
    users.create_user_with_playlist_and_song()
    user = User(data.user_name)
    song = Song()
    assert asserts.down_vote_song(song, user, data.playlist), data.assert_down_vote_song
