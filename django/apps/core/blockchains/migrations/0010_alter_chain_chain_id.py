# Generated by Django 4.2.16 on 2024-10-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blockchains", "0009_microdenom_alter_chain_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chain",
            name="chain_id",
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
