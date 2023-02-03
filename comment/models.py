from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class Comment(models.Model):
    body = models.TextField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + str(self.post.city)
