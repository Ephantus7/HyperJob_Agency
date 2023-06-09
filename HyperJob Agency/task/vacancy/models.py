from django.db import models
from django.contrib.auth.models import User


class Vacancy(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024)
