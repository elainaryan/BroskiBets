# Generated by Django 3.2.6 on 2021-08-28 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0006_dailypicks_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailypicks',
            name='pub_date',
            field=models.DateField(default=datetime.datetime),
        ),
    ]