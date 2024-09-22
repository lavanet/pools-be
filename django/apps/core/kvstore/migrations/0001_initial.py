# Generated by Django 4.2.16 on 2024-09-22 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyValue',
            fields=[
                ('key', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('value', models.JSONField(default=dict)),
            ],
        ),
    ]
