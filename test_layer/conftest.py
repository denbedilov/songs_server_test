import pytest
from logic_layer import users, songs


@pytest.fixture(scope="function")
def remove_users():
    users.remove_all_users()


@pytest.fixture(scope="function")
def remove_songs():
    songs.remove_all_songs()
