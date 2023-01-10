from django.test import TestCase
from django.contrib.auth.models import User
from post.models import Post
from upvote.models import Upvote
from review.models import Review
from django.urls import reverse

class UpvoteTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test_user", password="pass",)

    def setUp(self):
        self.client.force_login(self.user)

    def test_user_create_upvote(self):
        post = Post.objects.create()
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
        response = self.client.post(reverse('create_upvote'), data={
            'review_id': review.id,
            'post_id': post.id
        })
        review_upvote = review.number_of_upvotes
        upvote = Upvote.objects.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(upvote), 1)
        self.assertEqual(review_upvote, 1)

class UpvoteDestroy(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test_user", password="pass",)
        cls.post = Post.objects.create()
        cls.review = Review.objects.create(post_id=cls.post.id,
            user_id=cls.user.id,
            body="Body test",
            header="Header test",
            internet=5,
            hospitality=5,
            fun=5,
            cost=5,
            safety=5,
            life_quality=5,
            score=5)
    
    def setUp(self):
        self.client.force_login(self.user)

    def test_user_destroy_upvote(self):
        Upvote.objects.create(review=self.review, user=self.user)
        response = self.client.post(reverse('destroy_upvote'), data={
            'review_id': self.review.id,
            'post_id': self.post.id
        })
        upvote = Upvote.objects.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(upvote), 0)
