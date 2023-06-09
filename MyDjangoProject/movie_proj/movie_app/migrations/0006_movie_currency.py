# Generated by Django 4.1.7 on 2023-04-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0005_alter_movie_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="currency",
            field=models.CharField(
                choices=[("E", "Euro"), ("D", "Dollars"), ("R", "Rubles")],
                default="R",
                max_length=1,
            ),
        ),
    ]
