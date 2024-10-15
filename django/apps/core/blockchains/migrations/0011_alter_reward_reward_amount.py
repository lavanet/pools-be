# Generated by Django 4.2.16 on 2024-10-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blockchains", "0010_alter_chain_chain_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reward",
            name="reward_amount",
            field=models.DecimalField(decimal_places=12, default=0, max_digits=36),
        ),
        migrations.AlterField(
            model_name="chain",
            name="future_rewards",
            field=models.DecimalField(decimal_places=12, default=0, max_digits=36),
        ),
        migrations.AlterField(
            model_name="chain",
            name="past_rewards",
            field=models.DecimalField(decimal_places=12, default=0, max_digits=36),
        ),
        migrations.AlterField(
            model_name="chain",
            name="rewards_per_month",
            field=models.DecimalField(decimal_places=12, default=0, max_digits=36),
        ),
        migrations.AlterField(
            model_name="denom",
            name="price",
            field=models.DecimalField(
                decimal_places=12, default=0, max_digits=36, verbose_name="Price (USD)"
            ),
        ),
    ]
