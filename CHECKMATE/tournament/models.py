from django.db import models


# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField()

    def __str__(self):
        return f"{self.name}"
