# Generated by Django 3.2.6 on 2021-08-31 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0009_auto_20210829_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailypicks',
            name='title',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]