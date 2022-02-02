import pytest
from logic_layer import songs, data


@pytest.mark.basic
@pytest.mark.songs
def test_add_song(remove_songs):
    songs.add_song(data.song)
    res = songs.get_song(data.song)
    expected = data.get_song
    assert res, expected


@pytest.mark.basic
@pytest.mark.songs
def test_get_song(remove_songs):
    songs.add_song(data.song)
    res = songs.get_song(data.song)
    expected = data.get_song
    assert res, expected
