from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'movie_table'