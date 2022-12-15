from django.db import models
from post.models import Post

class Review(models.Model):
    header = models.CharField(max_length=90)
    body = models.TextField(max_length=800)
    score = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    # user onetoone -- https://docs.djangoproject.com/en/4.1/topics/db/examples/one_to_one/

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return str(self.id) + str(self.post.city)