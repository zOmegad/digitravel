from django.urls import reverse
from django.test import TestCase

from post.models import Post


class IndexPageTestCase(TestCase):
    def test_index_page_returns_200(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
class ShowPageTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            city = "Paris",
            country = "France",
            language = "FRA",
            population = 10000,
            longitude = 1.102,
            latitude = 2.021,
            currency = "EUR",
            continent = "Europe",
            region = "West Europe")
        self.post = Post.objects.first()

    def test_show_with_product_returns_200(self):
        response = self.client.get(reverse('show', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
