import pytest
from logic_layer import asserts, user, data, song


@pytest.mark.basic
@pytest.mark.playlists
def test_add_song_to_playlist(remove_users, remove_songs):
    u = user.User(data.user_name)
    s = song.Song()
    playlist_name = 'playlist'
    assert asserts.add_user(u), data.assert_add_user
    assert asserts.add_playlist(u, playlist_name), data.assert_add_playlist
    assert asserts.add_song(s), data.assert_add_song
    assert asserts.add_song_to_playlist(u, playlist_name, s.get_title()), data.assert_add_song_to_playlist
