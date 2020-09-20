from django.db import models
from django.urls import reverse
Ratings=[
    ('1','*'),
    ('2','**'),
    ('3','***'),
    ('4','****'),
    ('5','*****')
]
# Create your models here.

class Theatre(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Movies(models.Model):
    name=models.CharField(max_length=20)
    theatre=models.ForeignKey(Theatre,on_delete=models.CASCADE)
    characters=models.TextField()
    tags=models.CharField(max_length=20)
    IMDb_rating=models.CharField(default='3',max_length=1,choices=Ratings)
    ticket_price=models.CharField(max_length=4)
    poster=models.ImageField(upload_to='banner')
    duration=models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie_list')
