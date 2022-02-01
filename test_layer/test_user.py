import unittest
from logic_layer import users, data


class TestUserLogic(unittest.TestCase):
    def test_add_user(self):
        users.add_user(data.user)
        res = users.get_user(data.user)
        expected = data.get_user
        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
