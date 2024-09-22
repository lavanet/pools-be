# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSent',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('sent_to', models.CharField(max_length=256, verbose_name='Sent to email')),
                ('template', models.CharField(max_length=256, verbose_name='Template')),
                ('content', models.TextField(verbose_name='Content')),
                ('timestamp', models.DateTimeField(verbose_name='Timestamp', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Emails sent',
                'verbose_name': 'Email sent',
            },
        ),
    ]
