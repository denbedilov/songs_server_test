import pytest
from logic_layer import asserts, data
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
