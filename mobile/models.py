from django.db import models
from django.db import models
from django.core.validators import MinValueValidator

class MobileInfo(models.Model):
    OPTION_CHOICES = [
        (0, '-'),
        (1, '+')
    ]

    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    mobile_type = models.CharField(max_length=30, unique=True)
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)])  
    color = models.CharField(max_length=20)
    screen_size = models.FloatField()  
    check_exist = models.IntegerField(choices=OPTION_CHOICES, default=1)
    country = models.CharField(max_length=20)
    count = models.PositiveIntegerField(default=1)  


    def save(self, *args, **kwargs):
        
        if self.count == 0:
            self.check_exist = 0
        super().save(*args, **kwargs)

    