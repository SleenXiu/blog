# coding=utf-8
# created by sleen 
# test_user_model.py 单元测试

import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):

    def test_password_setter(self):
        u = User(password = 'cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password = 'cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password = 'cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertTrue(u.verify_password('dog'))

    def test_password_salts_are_radom(self):
        u = User(password = 'cat')
        u2 = User(password = 'dog')
        self.assertTrue(u.password_hash != u2.password_hash)