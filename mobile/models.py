from django.db import models

class MoblieInfo(models.Model):

    OPTION_CHOICES = [
        (0, '-'),
        (1, '+')
    ]


    Name = models.CharField(max_length=20)
    Nationality = models.CharField(max_length=20)
    Type = models.CharField(max_length=30, unique=True)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    screenSize = models.PositiveIntegerField()
    checkExist = models.IntegerField(choices=OPTION_CHOICES, default=0)
    country = models.CharField(max_length=20)
