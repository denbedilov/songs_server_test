import pytest

from logic_layer import users, data


# test basic user actions
# test add new user
@pytest.mark.basic
def test_add_user(remove_users):
    users.add_user(data.user)
    res = users.get_user(data.user)
    expected = data.get_user
    assert res, expected


# test get user
@pytest.mark.basic
def test_get_user(remove_users):
    users.add_user(data.user)
    res = users.get_user(data.user)
    expected = data.get_user
    assert res, expected


# test add friend
@pytest.mark.basic
def test_add_friend(remove_users):
    users.add_user(data.user_with_friend)
    users.add_friend(data.user_with_friend)
    res = users.get_user(data.user_with_friend)
    expected = data.get_user_with_friend
    assert res, expected


# test change password
@pytest.mark.basic
def test_change_password(remove_users):
    users.add_user(data.user_with_pass)
    res = users.change_password(data.user_with_pass)
    expected = data.get_user_with_pass
    assert res, expected
