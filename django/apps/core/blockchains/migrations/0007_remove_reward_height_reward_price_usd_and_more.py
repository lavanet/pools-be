# Generated by Django 4.2.16 on 2024-10-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "blockchains",
            "0006_chain_rpc_url_alter_chain_network_alter_denom_price_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reward",
            name="height",
        ),
        migrations.AddField(
            model_name="reward",
            name="price_usd",
            field=models.DecimalField(
                blank=True, decimal_places=4, default=0, max_digits=16
            ),
        ),
        migrations.AlterField(
            model_name="reward",
            name="reward_amount",
            field=models.DecimalField(decimal_places=18, default=0, max_digits=32),
        ),
    ]
