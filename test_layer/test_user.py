from logic_layer import users, data


# test add new user
def test_add_user(remove_users):
    users.add_user(data.user)
    res = users.get_user(data.user)
    expected = data.get_user
    assert res, expected


# test get user
def test_get_user(remove_users):
    users.add_user(data.user)
    res = users.get_user(data.user)
    expected = data.get_user
    assert res, expected


# test add friend
def test_add_friend(remove_users):
    users.add_user(data.user_with_friend)
    users.add_friend(data.user_with_friend)
    res = users.get_user(data.user_with_friend)
    expected = data.get_user_with_friend
    assert res, expected



