import pytest
from logic_layer import users


@pytest.fixture
def remove_users():
    users.remove_all_users()
