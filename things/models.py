from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(AbstractUser):
    name = models.CharField(blank = False, max_length=30, unique = True)
    description = models.TextField(blank = True, max_length=120, unique = False)
    quantity = models.IntegerField()#unique = False, 
                                   #validators = [MinValueValidator(1), 
                                    #           MaxValueValidator(100)] )