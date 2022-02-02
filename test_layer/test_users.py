import pytest
from logic_layer import users, data


# test basic user actions
# test add new user
@pytest.mark.basic
@pytest.mark.users
def test_add_user(remove_users):
    users.add_user(data.user)
    res = users.get_user(data.user)
    expected = data.get_user
    assert res, expected


# test get user
@pytest.mark.basic
@pytest.mark.users
def test_get_user(remove_users):
    users.add_user(data.user)
    res = users.get_user(data.user)
    expected = data.get_user
    assert res, expected


# test add friend
@pytest.mark.basic
@pytest.mark.users
def test_add_friend(remove_users):
    users.add_user(data.user_with_friend)
    users.add_friend(data.user_with_friend)
    res = users.get_user(data.user_with_friend)
    expected = data.get_user_with_friend
    assert res, expected


# test change password
@pytest.mark.basic
@pytest.mark.users
def test_change_password(remove_users):
    users.add_user(data.user_with_pass)
    res = users.change_password(data.user_with_pass)
    expected = data.get_user_with_pass
    assert res, expected
    # TODO add another check? something needs a new password


# test add playlist
@pytest.mark.basic
@pytest.mark.users
def test_add_playlist(remove_users):
    users.add_user(data.user_with_playlist)
    res = users.get_user(data.user_with_playlist)
    expected = data.get_user_with_playlist
    assert res, expected


# test get playlist
@pytest.mark.basic
@pytest.mark.users
def test_get_playlist(remove_users):
    users.add_user(data.user_with_playlist)
    res = users.get_user(data.user_with_playlist)
    expected = data.get_user_with_playlist
    assert res, expected
