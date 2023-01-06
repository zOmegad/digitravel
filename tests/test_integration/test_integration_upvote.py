from django.test import TestCase
from django.contrib.auth.models import User
from post.models import Post
from upvote.models import Upvote
from review.models import Review
from django.urls import reverse

class UpvoteTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="pass",)
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
        upvote = Upvote.objects.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(upvote), 1)

class UpvoteDestroy(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="pass",)
        self.client.force_login(self.user)

    def test_user_destroy_upvote(self):
        post = Post.objects.create()
        u = Upvote.objects.all()
        print(u)
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
        Upvote.objects.create(review=review, user=self.user)

        response = self.client.post(reverse('create_upvote'), data={
            'review_id': review.id,
            'post_id': post.id
        })
        upvote = Upvote.objects.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(upvote), 0)