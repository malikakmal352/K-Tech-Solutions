from django.db import models

# Create your models here.
class Brand(models.Model):
    Brand_name = models.CharField(max_length=100)

    @staticmethod
    def get_all_Category():
        return Brand.objects.all()

    def __str__(self):
        return self.Brand_name