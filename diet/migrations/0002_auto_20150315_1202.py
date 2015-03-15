# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
