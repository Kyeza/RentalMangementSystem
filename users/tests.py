from django.test import TestCase

from users.models import User


class TestUserModel(TestCase):

    @staticmethod
    def create_user(username, email, password):
        return User.objects.create_user(username=username, email=email, password=password)

    def test_user_creation(self):
        user = self.create_user('testUser', 'test@gmail.com', '12345678')

        self.assertEqual(user.username, 'testUser')
        self.assertTrue(user.check_password('12345678'))

        user.first_name = 'test'
        user.save()
        self.assertTrue(user.first_name, 'test')

        user.set_password('test12345')
        user.save()
        self.assertFalse(user.check_password('12345678'))
