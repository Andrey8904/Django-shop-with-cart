from django.test import TestCase
from .models import CustomUser

class UserViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(
            user_name='test_user',
            user_email='test@test.com',
            user_password='123',
            user_agree=True
        )

    def test_user_create(self):
        user = CustomUser.objects.get(user_name='test_user')
        self.assertEqual(user.user_name, 'test_user')
        self.assertEqual(user.user_email, 'test@test.com')
        self.assertEqual(user.user_password, '123')
        self.assertTrue(user.user_agree)
        self.assertFalse(user.user_banned)
        self.assertFalse(user.user_activated)

    def test_user_str_resp(self):
        user = CustomUser.objects.get(user_name='test_user')
        self.assertEqual(str(user), 'test_user')
