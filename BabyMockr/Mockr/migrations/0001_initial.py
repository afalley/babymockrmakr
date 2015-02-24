# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BabyName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('rank', models.IntegerField(default=0, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mock_text', models.CharField(max_length=400)),
                ('rhyming', models.BooleanField(default=False)),
                ('is_parents_favorite', models.BooleanField(default=False)),
                ('baby_name', models.ForeignKey(related_name='babyname', to='Mockr.BabyName')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MockRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brutality', models.IntegerField(default=0)),
                ('stupidity', models.IntegerField(default=0)),
                ('funny', models.IntegerField(default=0)),
                ('overall', models.IntegerField(default=0, blank=True)),
                ('mock', models.ForeignKey(to='Mockr.Mock')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MockrUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_facebook_user', models.BooleanField(default=False)),
                ('is_mockr', models.BooleanField(default=False)),
                ('mockr_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mockrating',
            name='mockr_user',
            field=models.ForeignKey(to='Mockr.MockrUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mock',
            name='mockr_user',
            field=models.ForeignKey(related_name='mockruser', to='Mockr.MockrUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favorite',
            name='mockr_user',
            field=models.ForeignKey(to='Mockr.MockrUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favorite',
            name='mocks',
            field=models.ForeignKey(to='Mockr.Mock'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='babyname',
            name='mockr_user',
            field=models.ForeignKey(related_name='mkuser', to='Mockr.MockrUser'),
            preserve_default=True,
        ),
    ]
