import pytest
from logic_layer import asserts, data, user
from logic_layer.song import Song


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
    u = user.User('user')
    s = Song()
    playlist = 'playlist'
    assert asserts.add_song(s), data.assert_add_song
    assert asserts.upvote_song(s, u, playlist), data.assert_upvote_song
    assert asserts.get_song(s), data.assert_get_song


@pytest.mark.basic
@pytest.mark.songs
def test_down_vote(remove_songs):
    u = user.User('user')
    s = Song()
    playlist = 'playlist'
    assert asserts.add_song(s), data.assert_add_song
    assert asserts.upvote_song(s, u, playlist), data.assert_upvote_song
    assert asserts.down_vote_song(s, u, playlist), data.assert_down_vote_song
    assert asserts.get_song(s), data.assert_get_song
