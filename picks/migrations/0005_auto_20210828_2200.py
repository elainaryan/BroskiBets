# Generated by Django 3.2.6 on 2021-08-28 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0004_singlepick'),
    ]

    operations = [
        migrations.CreateModel(
            name='KanePick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_text', models.CharField(max_length=200)),
                ('daily_picks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picks.dailypicks')),
            ],
            options={
                'verbose_name': "Kane's Pick",
                'verbose_name_plural': "Kane's Picks",
            },
        ),
        migrations.CreateModel(
            name='ScottPick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_text', models.CharField(max_length=200)),
                ('daily_picks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picks.dailypicks')),
            ],
            options={
                'verbose_name': "Scott's Pick",
                'verbose_name_plural': "Scott's Picks",
            },
        ),
        migrations.DeleteModel(
            name='SinglePick',
        ),
    ]