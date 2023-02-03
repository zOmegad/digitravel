from django.db import models
from django.contrib.auth.models import User
from review.models import Review


class Upvote(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user"
    )

    class Meta:
        unique_together = (
            "user",
            "review",
        )
