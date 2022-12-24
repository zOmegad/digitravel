from django.test import TestCase

class SignUpTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'Rg^K,4ybA"3*PdP[>e^s8'

    def test_signup_returns_page(self):
        response = self.client.get('/sign_up/')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        response = self.client.post('/sign_up/', data={
            'username': self.username,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)

