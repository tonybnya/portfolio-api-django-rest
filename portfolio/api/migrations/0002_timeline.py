# Generated by Django 4.2.13 on 2024-05-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Timeline",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.CharField(max_length=50)),
                ("milestone", models.CharField(max_length=200)),
                ("duration", models.CharField(max_length=50)),
                ("details", models.TextField()),
            ],
        ),
    ]
