# Generated by Django 5.1.5 on 2025-01-29 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("clients", "0001_initial"),
        ("currencies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DataEntry",
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
                (
                    "transaction_type",
                    models.CharField(
                        choices=[("income", "Income"), ("expense", "Expense")],
                        max_length=7,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField()),
                ("cross_rate", models.DecimalField(decimal_places=4, max_digits=10)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="clients.client"
                    ),
                ),
                (
                    "currency_in",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="currency_in",
                        to="currencies.currency",
                    ),
                ),
                (
                    "currency_out",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="currency_out",
                        to="currencies.currency",
                    ),
                ),
            ],
        ),
    ]
