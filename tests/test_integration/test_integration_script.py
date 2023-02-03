from django.core.management import call_command
from django.test import TestCase
from post.models import Post


class CommandsTestCase(TestCase):
    def test_mycommand(self):
        call_command("post_inject", min_population=10000000, keep_db=True)
        posts = Post.objects.all()
        self.assertEqual(len(posts), 40)
