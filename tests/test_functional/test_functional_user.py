from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.urls import reverse
from django.contrib.auth.models import User


class TestUserTests(StaticLiveServerTestCase):
    def setUp(self):
        driver_path = "./tests/test_functional/chromedriver"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.browser =  webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path)
        self.test_host = self.live_server_url

    def tearDown(self) :
        self.browser.close()

    def test_user_sign_up(self):
        signup_url = reverse('signup')
        self.browser.get(f'{self.test_host}{signup_url}')
        input_username= self.browser.find_element(By.ID, "username")
        input_password1= self.browser.find_element(By.ID, "password1")
        input_password2= self.browser.find_element(By.ID, "password2")

        input_username.send_keys("test_user")
        input_password1.send_keys("AZErty123*")
        input_password2.send_keys("AZErty123*")
        form_element = self.browser.find_element(By.ID, "submit-button")
        form_element.click()
        self.assertEqual(self.browser.current_url, f"{self.test_host}/post/")
    
    def test_user_login(self):
        User.objects.create_user("test_user", "test@test.io", "AZErty123*")
        login_url = reverse('login')
        self.browser.get(f'{self.test_host}{login_url}')
        input_username= self.browser.find_element(By.ID, "username")
        input_password= self.browser.find_element(By.ID, "password")

        input_username.send_keys("test_user")
        input_password.send_keys("AZErty123*")
        form_element = self.browser.find_element(By.ID, "submit-button")
        form_element.click()
        self.assertEqual(self.browser.current_url, f"{self.test_host}/")
    