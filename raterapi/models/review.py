from django.db import models

class Reviews(models.Model):
    review = models.CharField(max_length=300)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)