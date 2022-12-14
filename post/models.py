from django.db import models

class Post(models.Model):
    city = models.CharField(max_length=40, unique=True)
    country = models.CharField(max_length=40)
    language = models.CharField(max_length=40)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.city