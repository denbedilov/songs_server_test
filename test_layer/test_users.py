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
    assert asserts.add_friend(user, data.friend_name), data.assert_add_friend
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
    assert asserts.add_playlist(user, data.playlist), data.assert_add_playlist
    assert asserts.get_playlist(user), data.assert_get_playlist


# test get playlist
@pytest.mark.basic
@pytest.mark.users
def test_get_playlist(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    assert asserts.add_playlist(user, data.playlist), data.assert_add_playlist
    assert asserts.get_playlist(user), data.assert_get_playlist


# test add same user
@pytest.mark.sys_req
@pytest.mark.users
def test_add_same_user(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    assert asserts.add_user(user, fail=True), data.assert_double_user


# test get users with all fields (at least two friends and two playlists)
@pytest.mark.sys_req
@pytest.mark.users
def test_get_full_user(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    assert asserts.add_friend(user, data.friend_name), data.assert_add_friend
    assert asserts.add_friend(user, data.friend_name2), data.assert_add_friend
    assert asserts.add_playlist(user, data.playlist), data.assert_add_playlist
    assert asserts.add_playlist(user, data.playlist2), data.assert_add_playlist


# test all actions required password with no password
@pytest.mark.sys_req
@pytest.mark.users
@pytest.mark.xfail
def test_password_required(remove_users):
    user = User(data.user_name, '')
    # assert asserts.add_user(user, fail=True), data.assert_add_user
    user.set_password(None)
    assert asserts.add_user(user, fail=True), data.assert_add_user
    user.set_password('pass')
    assert asserts.add_user(user), data.assert_add_user
    user.set_password('')
    assert asserts.add_friend(user, data.friend_name, fail=True), data.assert_add_friend
    user.set_password(None)
    assert asserts.add_friend(user, data.friend_name, fail=True), data.assert_add_friend
    user.set_password('pass')
    assert asserts.add_friend(user, data.friend_name), data.assert_add_friend
    user.set_password('')
    assert asserts.add_playlist(user, data.playlist, fail=True), data.assert_add_playlist
    user.set_password(None)
    assert asserts.add_playlist(user, data.playlist, fail=True), data.assert_add_playlist
    user.set_password('pass')
    assert asserts.add_playlist(user, data.playlist), data.assert_add_playlist
    # TODO: check pass change password
    # TODO: check password get playlist
    # TODO: check password upvote
    # TODO: check password down vote
    # TODO: check password add song to playlist

