from django.db import models


class Post(models.Model):
    city = models.CharField(max_length=40, unique=True)
    country = models.CharField(max_length=40)
    language = models.CharField(max_length=40)
    population = models.IntegerField(default=0)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    currency = models.CharField(max_length=10, blank=True)
    continent = models.CharField(max_length=20)
    region = models.CharField(max_length=30)

    def __str__(self):
        return "Id: {} | City: {} ".format(self.id, self.city)

    # return avg of scores according to field arg
    def post_score(self, field):
        from django.db.models import Avg
        from review.models import Review

        my_review = Review.objects.filter(post_id=self.id)
        post_score = my_review.aggregate(avg_rating=Avg(field))
        return post_score

    @property
    def post_index_score(self):
        from django.db.models import Avg
        from review.models import Review

        my_review = Review.objects.filter(post_id=self.id)
        post_score = my_review.aggregate(avg_rating=Avg("score"))
        return post_score

    class Meta:
        ordering = ("review",)


class Photo(models.Model):
    image = models.ImageField(blank=True)
    image_url = models.CharField(blank=True, max_length=200)
    author = models.CharField(blank=True, max_length=90)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
