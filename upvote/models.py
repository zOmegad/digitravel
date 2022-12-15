from django.db import models
from django.contrib.auth.models import User
from post.models import Post

class Upvote(models.Model):
    upvoted = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)