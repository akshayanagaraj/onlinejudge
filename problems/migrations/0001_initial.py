# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pid', models.CharField(max_length=10)),
                ('total', models.IntegerField(default=0)),
                ('tle', models.IntegerField(default=0)),
                ('acc', models.IntegerField(default=0)),
                ('wa', models.IntegerField(default=0)),
                ('ce', models.IntegerField(default=0)),
                ('rte', models.IntegerField(default=0)),
                ('accuracy', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('pid', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=10000)),
                ('sample_input', models.TextField(max_length=10000)),
                ('sample_output', models.TextField(max_length=10000)),
                ('explanation', models.TextField(max_length=10000)),
                ('is_active', models.BooleanField(default=False)),
                ('testfiles', models.IntegerField(default=0)),
                ('time_limit', models.FloatField(default=0)),
                ('details', models.ForeignKey(to='problems.Detail')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('sid', models.AutoField(serialize=False, primary_key=True)),
                ('code', models.FileField(null=True, upload_to=b'submissions', blank=True)),
                ('language', models.CharField(max_length=10)),
                ('subtime', models.DateTimeField()),
                ('status', models.CharField(default=b'waiting', max_length=20)),
                ('extime', models.FloatField(default=0)),
                ('errorcode', models.TextField(max_length=1000)),
                ('prob', models.ForeignKey(to='problems.Problem')),
                ('user', models.ForeignKey(to='users.OjUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
