from django.test import TestCase
from django.urls import reverse

class UserTestCase(TestCase):
    def test_login_page_returns_200(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_password_reset_returns_200(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_returns_login_if_not_logged_in(self):
        response = self.client.get(reverse('password_change'))
        self.assertEqual(response.url, "/accounts/login/?next=/accounts/password_change/")