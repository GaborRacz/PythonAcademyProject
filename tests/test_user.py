import unittest

from users import User
from usergen import generator

class TestUser(unittest.TestCase):
    """Test the user class"""

    def test_creation(self):
        user_generator = generator.UserGenerator()
        user = user_generator.generate_user()

    def test_names(self):
        user_generator = generator.UserGenerator()
        user = user_generator.generate_user()
        self.assertTrue(user.first_name == user.first_name.title())
        self.assertTrue(user.family_name == user.family_name.title())

    def test_email(self):
        user_generator = generator.UserGenerator()
        for i in xrange(100):
            user = user_generator.generate_user()
            self.assertTrue('@' in user.email)
            self.assertTrue(any(domain in user.email for domain in generator.email_domains))


