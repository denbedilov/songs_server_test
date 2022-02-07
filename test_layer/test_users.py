import pytest
from logic_layer import asserts, data, users
from logic_layer.user import User
from logic_layer.song import Song


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
    assert asserts.change_password(user, 'new_pass'), data.assert_change_password
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
# test add user password required
@pytest.mark.sys_req
@pytest.mark.users
@pytest.mark.xfail
def test_password_required_add_user(remove_users):
    user = User(data.user_name, '')
    assert asserts.add_user(user, fail=True), data.assert_add_user
    user.set_password(None)
    assert asserts.add_user(user, fail=True), data.assert_add_user
    user.set_password('pass')
    assert asserts.add_user(user), data.assert_add_user


@pytest.mark.sys_req
@pytest.mark.users
def test_password_required_add_friend(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    user.set_password('')
    assert asserts.add_friend(user, data.friend_name, fail=True), data.assert_add_friend
    user.set_password(None)
    assert asserts.add_friend(user, data.friend_name, fail=True), data.assert_add_friend
    user.set_password('pass')
    assert asserts.add_friend(user, data.friend_name), data.assert_add_friend


@pytest.mark.sys_req
@pytest.mark.users
def test_password_required_add_playlist(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    user.set_password('')
    assert asserts.add_playlist(user, data.playlist, fail=True), data.assert_add_playlist
    user.set_password(None)
    assert asserts.add_playlist(user, data.playlist, fail=True), data.assert_add_playlist
    user.set_password('pass')
    assert asserts.add_playlist(user, data.playlist), data.assert_add_playlist


@pytest.mark.sys_req
@pytest.mark.users
def test_password_required_change_password(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    user.set_password('')
    assert asserts.change_password(user, data.password, fail=True), data.assert_change_password
    user.set_password(None)
    assert asserts.change_password(user, data.password, fail=True), data.assert_change_password
    user.set_password('pass')
    assert asserts.change_password(user, data.password), data.assert_change_password


@pytest.mark.sys_req
@pytest.mark.users
def test_password_required_get_playlist(remove_users):
    user = User(data.user_name)
    assert asserts.add_user(user), data.assert_add_user
    assert asserts.add_playlist(user, data.playlist), data.assert_add_playlist
    user.set_password('')
    assert asserts.get_playlist(user, fail=True), data.assert_get_playlist
    user.set_password(None)
    assert asserts.get_playlist(user, fail=True), data.assert_get_playlist


# first time get to do prepare in one function
@pytest.mark.sys_req
@pytest.mark.users
def test_password_required_upvote(remove_users, remove_songs):
    user = User(data.user_name)
    song = Song()
    assert users.create_user_with_playlist_and_song(data.user_name, 'pass', data.playlist), data.assert_prepare_test
    user.set_password('')
    assert asserts.upvote_song(song, user, data.playlist, fail=True), data.assert_upvote_song
    user.set_password(None)
    assert asserts.upvote_song(song, user, data.playlist, fail=True), data.assert_upvote_song


@pytest.mark.sys_req
@pytest.mark.users
def test_password_required_down_vote(remove_users, remove_songs):
    user = User(data.user_name)
    song = Song()
    assert users.create_user_with_playlist_and_song(data.user_name, 'pass', data.playlist), data.assert_prepare_test
    user.set_password('')
    assert asserts.down_vote_song(song, user, data.playlist, fail=True), data.assert_upvote_song
    user.set_password(None)
    assert asserts.down_vote_song(song, user, data.playlist, fail=True), data.assert_upvote_song


@pytest.mark.sys_req
@pytest.mark.users
def test_password_required_add_song_to_playlist(remove_users):
    user = User(data.user_name)
    assert users.create_user_with_playlist(), data.assert_prepare_test
    song = Song()
    user.set_password('')
    assert asserts.add_song_to_playlist(user, data.playlist, song.get_title(), fail=True), \
        data.assert_add_song_to_playlist
    user.set_password(None)
    assert asserts.add_song_to_playlist(user, data.playlist, song.get_title(), fail=True), \
        data.assert_add_song_to_playlist

