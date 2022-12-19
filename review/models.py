from django.db import models
from django.contrib.auth.models import User
from post.models import Post

class Review(models.Model):
    header = models.CharField(max_length=90)
    body = models.TextField(max_length=800)
    score = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return str(self.post.city)
    
    class Meta:
        unique_together = ('user', 'post',)