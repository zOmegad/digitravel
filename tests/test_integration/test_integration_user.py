from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


class SignUpTestCase(TestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = 'Rg^K,4ybA"3*PdP[>e^s8'

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            data={
                "username": self.username,
                "password1": self.password,
                "password2": self.password,
            },
        )
        self.assertEqual(response.wsgi_request.user.username, self.username)
        self.assertEqual(
            response.status_code, 302
        )  # return 200 if password fails

    def test_login_form(self):
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        response = self.client.post(
            reverse("login"),
            data={"username": self.username, "password": self.password},
        )
        self.assertEqual(response.url, "/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.wsgi_request.user.username, self.username)

    def test_logout(self):
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.client.force_login(self.user)
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.wsgi_request.user.username, "")

    def test_destroy_with_correct_password(self):
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("destroy_user"), data={"password": self.password}
        )
        user = User.objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")
        self.assertEqual(user, None)

    def test_destroy_with_incorrect_password(self):
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("destroy_user"), data={"password": "caribou"}
        )
        user = User.objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/profile/")
        self.assertEqual(user, self.user)
