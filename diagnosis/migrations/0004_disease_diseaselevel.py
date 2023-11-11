# Generated by Django 4.2.7 on 2023-11-11 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("diagnosis", "0003_diagnosis_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Disease",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("yellow_rust", "Yellow Rust"),
                            ("black_rust", "Black Rust"),
                            ("brown_rust", "Brown Rust"),
                            ("septoria", "Septoria"),
                            ("powdery_mildew", "Powdery Mildew"),
                        ],
                        max_length=100,
                        unique=True,
                    ),
                ),
                ("description", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DiseaseLevel",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("level", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField()),
                (
                    "disease",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="levels",
                        to="diagnosis.disease",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]