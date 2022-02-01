import pytest
from logic_layer import users


@pytest.fixture(scope="function")
def remove_users():
    users.remove_all_users()
