# Generated by Django 4.0.6 on 2022-09-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_rename_genres_film_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(related_name='genre', to='backend.genre'),
        ),
    ]
