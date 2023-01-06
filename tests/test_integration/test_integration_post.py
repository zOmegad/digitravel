from django.test import TestCase
from django.urls import reverse
from post.models import Post

class PostTestCase(TestCase):

    def test_create_post(self):
        post = Post.objects.create(
            city = 'City test',
            country = 'City country',
            language = 'EN',
            population = 10,
            longitude = 1.2,
            latitude = 3.4,
            currency = 'BTC',
            continent = 'EUROPE',
            region = 'West'
        )
        self.assertEqual(post.city, 'City test')
        self.assertEqual(post.country, 'City country')
        self.assertEqual(post.language, 'EN')
        self.assertEqual(post.population, 10)
        self.assertEqual(post.longitude, 1.2)
        self.assertEqual(post.latitude, 3.4)
        self.assertEqual(post.currency, 'BTC')
        self.assertEqual(post.continent, 'EUROPE')
        self.assertEqual(post.region, 'West')
    
    def test_search_post(self):
        post = Post.objects.create(city="Testing query search")
        response = self.client.get(reverse('search'), data={
            'query': "Testing query search"
        })
        response_no_result = self.client.get(reverse('search'), data={
            'query': "ddhjshdsjqdgsqhdakzjdbkqdhqqgbj"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'][0], post)
        self.assertEqual(len(response.context['post'].object_list), 1)
        self.assertEqual(response_no_result.status_code, 200) # catch IndexError
        self.assertEqual(len(response_no_result.context['post'].object_list), 0)

        