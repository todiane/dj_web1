# Generated by Django 5.0 on 2024-05-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
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
                ("user_image", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "rating_count",
                    models.IntegerField(
                        choices=[
                            (1, "One"),
                            (2, "Two"),
                            (3, "Three"),
                            (4, "Four"),
                            (5, "Five"),
                        ]
                    ),
                ),
                ("username", models.CharField(max_length=50)),
                ("user_job_title", models.CharField(max_length=50)),
                ("review", models.TextField()),
            ],
        ),
    ]