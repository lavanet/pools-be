# Generated by Django 4.2.16 on 2024-10-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blockchains", "0012_alter_blockrequest_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chain",
            name="estimated_apr",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
    ]
