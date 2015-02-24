# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mockr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='mockr_user',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='mocks',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
        migrations.AlterField(
            model_name='babyname',
            name='rank',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
