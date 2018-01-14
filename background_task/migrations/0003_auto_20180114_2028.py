# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-01-14 20:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('background_task', '0002_auto_20170927_1109'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='task',
            index_together=set([('task_name', 'task_hash'), ('locked_at', 'failed_at', 'run_at'), ('run_at', 'failed_at'), ('run_at', 'failed_at', 'queue')]),
        ),
    ]
