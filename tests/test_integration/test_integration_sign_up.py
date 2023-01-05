from django.urls import reverse
from django.test import TestCase

class SignUpTestCase(TestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'Rg^K,4ybA"3*PdP[>e^s8'

    def test_signup_form(self):
        response = self.client.post(reverse('signup'), data={
            'username': self.username,
            'password1': self.password,
            'password2': self.password
        })
        # return 200 if password fails
        self.assertEqual(response.status_code, 302)