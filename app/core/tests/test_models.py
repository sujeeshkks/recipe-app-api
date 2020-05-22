from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """Test create user with a an email succesful
        """
        email = 'sujeesh@djando.com'
        password = 'Django123'
        username = 'django'

        user = get_user_model().objects.create_user(
                email=email,
                password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):
        """Check email address in converted to lower case
        """
        email = 'test@DJANGO.COM'
        password = 'Django123'

        user = get_user_model().objects.create_user(
                email, password)

        self.assertEqual(user.email, email.lower())

    def test_invlaid_email_raises_value_error(self):
        email = None
        password = 'Django123'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email, password)

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser('test@django.com', 'djano123')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)