# Generated by Django 3.2.6 on 2021-08-28 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0003_alter_dailypicks_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='SinglePick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_text', models.CharField(max_length=200)),
                ('daily_picks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picks.dailypicks')),
            ],
        ),
    ]
