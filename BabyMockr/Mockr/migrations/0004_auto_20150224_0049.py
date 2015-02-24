# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mockr', '0003_auto_20150224_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babyname',
            name='rank',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
