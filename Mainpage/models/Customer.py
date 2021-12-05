from django.contrib.auth.models import User
from django.db import models


class customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
