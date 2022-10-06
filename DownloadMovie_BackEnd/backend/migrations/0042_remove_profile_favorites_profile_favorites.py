# Generated by Django 4.0.6 on 2022-10-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0041_profile_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorites',
        ),
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(null=True, to='backend.film'),
        ),
    ]