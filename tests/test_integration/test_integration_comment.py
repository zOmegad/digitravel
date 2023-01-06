from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from post.models import Post
from comment.models import Comment

class CommentTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="pass")
        self.client.force_login(self.user)

    def test_user_create_comment(self):
        post = Post.objects.create()
        response = self.client.post(reverse('create_comment'), data={
            'comment_body': "New comment test",
            'post_id': post.id
        })
        last_comment = Comment.objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(last_comment.body, 'New comment test')
        self.assertEqual(last_comment.post_id, post.id)
    
    def test_destroy_comment(self):
        post = Post.objects.create()
        comment = Comment.objects.create(body="Super comment",
            post= post,
            user=self.user)
        response = self.client.post(reverse('destroy_comment'), data={
            "comment_id": comment.id,
            'post_id': post.id,
        })
        comment = Comment.objects.all()
        self.assertEqual(len(comment), 0)
        self.assertEqual(response.status_code, 302)
