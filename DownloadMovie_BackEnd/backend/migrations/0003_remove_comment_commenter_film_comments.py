# Generated by Django 4.1 on 2022-08-19 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_film_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commenter',
        ),
        migrations.AddField(
            model_name='film',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.comment'),
        ),
    ]