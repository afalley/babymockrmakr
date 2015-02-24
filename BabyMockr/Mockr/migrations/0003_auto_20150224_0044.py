# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mockr', '0002_auto_20150223_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_favorite', models.BooleanField(default=False)),
                ('mockr_user', models.ForeignKey(to='Mockr.MockrUser')),
                ('mocks', models.ForeignKey(to='Mockr.Mock')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='babyname',
            name='rank',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
