# Generated by Django 4.0.6 on 2022-09-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0031_film_about_film_dislike_film_like_alter_film_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='double',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='subtitle',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='thumbnail',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='trailer',
            field=models.CharField(max_length=800, null=True),
        ),
    ]
