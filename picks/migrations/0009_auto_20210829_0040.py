# Generated by Django 3.2.6 on 2021-08-29 00:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0008_alter_dailypicks_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailypicks',
            name='test_text',
        ),
        migrations.AlterField(
            model_name='dailypicks',
            name='pub_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
