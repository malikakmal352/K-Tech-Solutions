from django.contrib.auth.models import User
from django.db import models


# class customer(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30, null=True)
#     email = models.EmailField(max_length=50)
#
#     def __str__(self):
#         return self.name


class customer(models.Model):
    name = models.CharField(max_length=200, default='')
    email = models.EmailField(default='')
    password = models.CharField(max_length=100, default='')
    Mn = models.IntegerField(default=0)

    def __str__(self):
        return self.email

    def get_by_email(email):
        try:
            return customer.objects.get(email=email)
        except:
            return False

    def isExits(self):
        if customer.objects.filter(email=self.email):
            return True

        return False
