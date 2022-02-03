import pytest
from logic_layer import asserts, data
from logic_layer.user import User


# test basic user actions
# test add new user
@pytest.mark.basic
@pytest.mark.users
def test_add_user(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    assert asserts.get_user(user), data.assert_get_user


# test get user
@pytest.mark.basic
@pytest.mark.users
def test_get_user(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    assert asserts.get_user(user), data.assert_get_user


# test add friend
@pytest.mark.basic
@pytest.mark.users
def test_add_friend(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    assert asserts.add_friend(user), data.assert_add_friend
    assert asserts.get_friend(user), data.assert_get_friend


# test change password
@pytest.mark.basic
@pytest.mark.users
def test_change_password(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    assert asserts.change_password(user), data.assert_change_password
    # TODO add another check? something needs a new password


# test add playlist
@pytest.mark.basic
@pytest.mark.users
def test_add_playlist(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    assert asserts.add_playlist(user), data.assert_add_playlist
    assert asserts.get_playlist(user), data.assert_get_playlist


# test get playlist
@pytest.mark.basic
@pytest.mark.users
def test_get_playlist(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    assert asserts.add_playlist(user), data.assert_add_playlist
    assert asserts.get_playlist(user), data.assert_get_playlist
