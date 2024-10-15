# Generated by Django 4.2.16 on 2024-10-08 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blockchains", "0004_denom_coingecko_last_update_alter_chain_denom"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chain",
            name="denom_price",
        ),
        migrations.AddField(
            model_name="chain",
            name="denom",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="chains",
                to="blockchains.denom",
            ),
        ),
    ]
