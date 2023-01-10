from django.test import TestCase
from django.contrib.auth.models import User
from post.models import Post
from review.models import Review
from django.urls import reverse

class ReviewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test_user", password="pass",)

    def setUp(self):
        self.client.force_login(self.user)

    def test_user_create_review(self):
        post = Post.objects.create(city='City test')
        response = self.client.post(reverse('create_review'), data={
                "body": 'Test body',
                "header": 'Test header',
                "internet": 5,
                "hospitality": 5,
                "fun": 5,
                "cost": 5,
                "safety": 5,
                "life_quality": 5,
                "post_id": post.id})
        review = Review.objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(review.body, 'Test body')
        self.assertEqual(review.header, 'Test header')
        self.assertEqual(review.internet, 5)
        self.assertEqual(review.hospitality, 5)
        self.assertEqual(review.fun, 5)
        self.assertEqual(review.cost, 5)
        self.assertEqual(review.safety, 5)
        self.assertEqual(review.life_quality, 5)
        self.assertEqual(review.score, 5)
        self.assertEqual(review.post_id, post.id)
        self.assertEqual(str(review), f"{review.id}{review.post.city}")

    def test_user_edit_review(self):
        post = Post.objects.create(city='City test')
        review = Review.objects.create(post_id=post.id,
            user_id=self.user.id,
            body="Body test",
            header="Header test",
            internet=5,
            hospitality=5,
            fun=5,
            cost=5,
            safety=5,
            life_quality=5,
            score=5)
        response = self.client.post(reverse('edit_review'), data={
            "body": 'Test edit body',
            "header": 'Test edit header',
            "internet": 4,
            "hospitality": 4,
            "fun": 4,
            "cost": 4,
            "safety": 4,
            "life_quality": 4,
            "post_id": review.post_id,
            "review_id": review.id})
        review = Review.objects.get(id=review.id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(review.body, 'Test edit body')
        self.assertEqual(review.header, 'Test edit header')
        self.assertEqual(review.internet, 4)
        self.assertEqual(review.hospitality, 4)
        self.assertEqual(review.fun, 4)
        self.assertEqual(review.cost, 4)
        self.assertEqual(review.safety, 4)
        self.assertEqual(review.life_quality, 4)
    
    def test_user_destroy_review(self):
        post = Post.objects.create(city='City test')
        review = Review.objects.create(post_id=post.id,
            user_id=self.user.id,
            body="Body test",
            header="Header test",
            internet=5,
            hospitality=5,
            fun=5,
            cost=5,
            safety=5,
            life_quality=5,
            score=5)
        response = self.client.post(reverse('destroy_review'), data={
            'review_id': review.id,
            'post_id': post.id
        })
        self.assertEqual(response.status_code, 302)