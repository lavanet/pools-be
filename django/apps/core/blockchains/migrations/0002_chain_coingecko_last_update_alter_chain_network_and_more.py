# Generated by Django 4.2.16 on 2024-10-08 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blockchains", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chain",
            name="coingecko_last_update",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="chain",
            name="network",
            field=models.CharField(
                choices=[("mainnet", "Mainnet"), ("testnet", "Testnet")],
                help_text="Tendermintrpc(lava.tendermintrpc.lava.build) or Testnet (lav1.tendermintrpc.lava.build) ",
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="reward",
            name="denom",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="rewards",
                to="blockchains.denom",
            ),
        ),
    ]
