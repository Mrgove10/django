from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Little(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)    
    weight = models.PositiveIntegerField()
