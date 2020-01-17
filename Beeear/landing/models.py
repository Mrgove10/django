from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class little(models.Model):
    name = models.CharField(),
    weight = models.PositiveIntegerField(),
    user = models.ForeignKey(User)
