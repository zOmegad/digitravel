from django.core.management import call_command
from io import StringIO
from django.test import TestCase
from post.models import Post

class CommandsTestCase(TestCase):
    def test_mycommand(self):
        opt = [10000000]
        call_command('post_inject', *opt, keep_db=True)
        posts = Post.objects.all()
        self.assertEqual(len(posts), 40)