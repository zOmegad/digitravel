from django.db import models
from post.models import Post

class Comment(models.Model):
    body = models.TextField(max_length=200, unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return str(self.id) + str(self.post.city)