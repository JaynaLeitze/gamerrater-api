from django.db import models

class Images(models.Model):
    image = models.ImageField(max_length=None, upload_to="games")