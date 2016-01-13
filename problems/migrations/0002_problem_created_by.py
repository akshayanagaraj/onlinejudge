# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='created_by',
            field=models.ForeignKey(blank=True, to='users.OjUser', null=True),
            preserve_default=True,
        ),
    ]
