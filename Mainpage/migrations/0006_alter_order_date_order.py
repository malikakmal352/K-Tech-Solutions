# Generated by Django 3.2.5 on 2021-12-13 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0005_alter_order_date_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 22, 59, 13, 257431), null=True),
        ),
    ]
