from django.db import models
from django.contrib.auth.models import User

class Upvote(models.Model):
    upvoted = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user')