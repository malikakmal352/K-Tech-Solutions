# Generated by Django 3.2.5 on 2021-12-05 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0002_auto_20211205_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 5, 20, 57, 33, 354981), null=True),
        ),
    ]