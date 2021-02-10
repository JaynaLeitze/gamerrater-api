from django.db import models

class Game(models.Model):
    
    title = models.CharField(max_length=75)
    description = models.TextField(max_length=300)
    designer = models.CharField(max_length=75)
    release_year = models.IntegerField()
    time_to_play = models.CharField (max_length=20)
    age_recommendation = models.IntegerField()