# Generated by Django 5.1.5 on 2025-01-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data_entries", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataentry",
            name="cross_rate",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
    ]
