# Generated by Django 3.2.6 on 2021-08-28 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0005_auto_20210828_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailypicks',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 28, 22, 4, 45, 989554)),
        ),
    ]
