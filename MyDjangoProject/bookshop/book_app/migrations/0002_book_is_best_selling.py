# Generated by Django 4.1.7 on 2023-04-15 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="is_best_selling",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]