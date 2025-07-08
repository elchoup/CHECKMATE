from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Player(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(110)]
    )
    global_score = models.IntegerField(default=0)
    tournament_score = models.IntegerField(default=0)
    index = models.IntegerField(null=True, blank=True)

    def __str__(self):
        name = f"{self.firstname} {self.lastname}"
        return f"Player {self.index}: {name}" if self.index != None else name
