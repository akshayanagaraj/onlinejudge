# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OjUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(max_length=3, null=True, blank=True)),
                ('reg_no', models.CharField(max_length=23, null=True, blank=True)),
                ('tot_sub', models.IntegerField(default=0)),
                ('succ_sub', models.IntegerField(default=0)),
                ('points', models.FloatField(default=0)),
                ('rank', models.IntegerField(default=1)),
                ('is_loggedin', models.BooleanField(default=False)),
                ('ex_time', models.FloatField(default=0.0)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
    ]
