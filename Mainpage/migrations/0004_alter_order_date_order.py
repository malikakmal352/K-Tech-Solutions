# Generated by Django 3.2.5 on 2021-12-05 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0003_alter_order_date_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 5, 21, 5, 24, 621728), null=True),
        ),
    ]
