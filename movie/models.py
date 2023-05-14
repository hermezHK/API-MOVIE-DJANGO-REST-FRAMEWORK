from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.CharField(max_length=50)
    image = models.TextField()
    country = models.CharField(max_length=50)
    duration = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "movies"
