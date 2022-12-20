from django.db import models
from upvote.models import Upvote

class Post(models.Model):
    city = models.CharField(max_length=40, unique=True)
    country = models.CharField(max_length=40)
    language = models.CharField(max_length=40)
    upvotes = models.ManyToManyField(Upvote, related_name="upvotes")

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "Id: {} | City: {} | Upvotes: {} ".format(self.id, self.city, self.upvotes.filter(upvoted=True).count())

    @property
    def post_score(self):
        from django.db.models import Avg
        from review.models import Review
        my_review = Review.objects.filter(post_id=self.id)
        post_score = my_review.aggregate(avg_rating=Avg('score'))
        return post_score

class Photo(models.Model):
    image = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)