from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class VisitorTestCase(TestCase):
    def test_login_page_returns_200(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_password_reset_returns_200(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_returns_login_if_not_logged_in(self):
        response = self.client.get(reverse('password_change'))
        self.assertEqual(response.url, "/accounts/login/?next=/accounts/password_change/")
        self.assertEqual(response.status_code, 302)
    
    def test_profile_page_redirect_if_logged_out(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.url, '/accounts/login/?next=/accounts/profile/')
        self.assertEqual(response.status_code, 302)

class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='Rg^K,4ybA"3*PdP[>e^s8')
        self.client.force_login(self.user)

    def test_user_access_profile(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
    
    def test_signup_redirects(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/post/")
