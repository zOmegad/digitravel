from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.urls import reverse


from post.models import Post

class TestUserTests(StaticLiveServerTestCase):
    def setUp(self):
        driver_path = "/Users/omegad/Documents/ocr/p13/digitravel/tests/test_functional/chromedriver"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.browser =  webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path)
        self.test_host = self.live_server_url

    def tearDown(self) :
        self.browser.close()
    
    def test_search_post(self):
        Post.objects.create(city="Lyon")
        Post.objects.create(city="Paris")
        self.browser.get(f'{self.test_host}')
        input_search= self.browser.find_element(By.ID, "search-input")
        submit_search= self.browser.find_element(By.ID, "search-submit")

        input_search.send_keys("Paris")
        submit_search.click()
        city_card = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div/a/h5")
        self.assertEqual(city_card.text, "Paris")
