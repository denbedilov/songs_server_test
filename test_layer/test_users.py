import pytest
from logic_layer import users
from logic_layer.user import User


# test basic user actions
# test add new user
@pytest.mark.basic
@pytest.mark.users
def test_add_user(remove_users):
    user = User('user')
    assert users.add_user(user.get_user()) == users.get_res_add_user(user.get_user())
    assert users.get_user(user.get_user()) == users.get_res_get_user(user.get_user_for_print())


# test get user
@pytest.mark.basic
@pytest.mark.users
def test_get_user(remove_users):
    user = User('user')
    assert users.add_user(user.get_user()) == users.get_res_add_user(user.get_user())
    assert users.get_user(user.get_user()) == users.get_res_get_user(user.get_user_for_print())


# test add friend
@pytest.mark.basic
@pytest.mark.users
def test_add_friend(remove_users):
    user = User('user')
    friend = 'friend'
    assert users.add_user(user.get_user()) == users.get_res_add_user(user.get_user())
    assert users.add_friend(user.add_item('friend_name', friend)) == users.get_res_add_friend(friend)
    assert users.get_user(user.add_friend(friend)) == users.get_res_get_user(user.get_user_for_print())


# test change password
@pytest.mark.basic
@pytest.mark.users
def test_change_password(remove_users):
    user = User('user')
    assert users.add_user(user.get_user()) == users.get_res_add_user(user.get_user())
    assert users.change_password(user.add_item('user_new_password', 'new_pass')) ==\
           users.get_res_change_password(user.get_user_for_print())
    # TODO add another check? something needs a new password


"""
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
"""