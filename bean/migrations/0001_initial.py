# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x9c\x8b\xe5\xae\xb6\xe5\x90\x8d\xe7\xa8\xb1')),
                ('description', models.TextField(default=b'', verbose_name=b'\xe5\x9c\x8b\xe5\xae\xb6\xe8\xaa\xaa\xe6\x98\x8e')),
            ],
            options={
                'verbose_name': '\u751f\u7522\u570b\u5bb6',
                'verbose_name_plural': '\u751f\u7522\u570b\u5bb6',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe7\xad\x89\xe7\xb4\x9a\xe5\x90\x8d\xe7\xa8\xb1')),
                ('description', models.TextField(default=b'', verbose_name=b'\xe7\xad\x89\xe7\xb4\x9a\xe8\xaa\xaa\xe6\x98\x8e')),
            ],
            options={
                'verbose_name': '\u751f\u8c46\u5206\u7d1a',
                'verbose_name_plural': '\u751f\u8c46\u5206\u7d1a',
            },
        ),
        migrations.CreateModel(
            name='OriginItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField(default=0)),
                ('engname', models.CharField(max_length=100, verbose_name=b'\xe7\x94\x9f\xe8\xb1\x86\xe8\x8b\xb1\xe6\x96\x87\xe5\x90\x8d\xe7\xa8\xb1')),
                ('chinesename', models.CharField(max_length=100, verbose_name=b'\xe7\x94\x9f\xe8\xb1\x86\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa8\xb1')),
                ('description', models.TextField(default=b'', verbose_name=b'\xe7\x94\x9f\xe8\xb1\x86\xe8\xaa\xaa\xe6\x98\x8e')),
                ('grade', models.ForeignKey(to='bean.Grade')),
            ],
            options={
                'verbose_name': '\u751f\u8c46\u9805\u76ee',
                'verbose_name_plural': '\u751f\u8c46\u9805\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('engname', models.CharField(max_length=40, verbose_name=b'\xe8\x8e\x8a\xe5\x9c\x92\xe8\x8b\xb1\xe6\x96\x87\xe5\x90\x8d\xe7\xa8\xb1')),
                ('chinesename', models.CharField(max_length=40, verbose_name=b'\xe8\x8e\x8a\xe5\x9c\x92\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe7\xa8\xb1')),
                ('description', models.TextField(default=b'', verbose_name=b'\xe8\x8e\x8a\xe5\x9c\x92\xe8\xaa\xaa\xe6\x98\x8e')),
                ('country', models.ForeignKey(to='bean.Country')),
            ],
            options={
                'verbose_name': '\u751f\u7522\u838a\u5712',
                'verbose_name_plural': '\u751f\u7522\u838a\u5712',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe8\x99\x95\xe7\x90\x86\xe5\x90\x8d\xe7\xa8\xb1')),
            ],
            options={
                'verbose_name': '\u8655\u7406\u65b9\u6cd5',
                'verbose_name_plural': '\u8655\u7406\u65b9\u6cd5',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x8d\x80\xe5\x9f\x9f\xe5\x90\x8d\xe7\xa8\xb1')),
            ],
            options={
                'verbose_name': '\u751f\u7522\u5340\u57df',
                'verbose_name_plural': '\u751f\u7522\u5340\u57df',
            },
        ),
        migrations.CreateModel(
            name='Roast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe7\x84\x99\xe5\xba\xa6\xe5\x90\x8d\xe7\xa8\xb1')),
                ('description', models.TextField(default=b'', verbose_name=b'\xe7\x84\x99\xe5\xba\xa6\xe8\xaa\xaa\xe6\x98\x8e')),
            ],
            options={
                'verbose_name': '\u70d8\u7119\u7119\u5ea6',
                'verbose_name_plural': '\u70d8\u7119\u7119\u5ea6',
            },
        ),
        migrations.CreateModel(
            name='RoastItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField(default=0)),
                ('aromadegree', models.IntegerField(default=3, verbose_name=b'\xe9\xa6\x99\xe6\xb0\xa3\xe7\xad\x89\xe7\xb4\x9a', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('sweetnessdegree', models.IntegerField(default=3, verbose_name=b'\xe7\x94\x9c\xe5\xba\xa6\xe7\xad\x89\xe7\xb4\x9a', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('aciditydegree', models.IntegerField(default=3, verbose_name=b'\xe9\x85\xb8\xe5\x91\xb3\xe7\xad\x89\xe7\xb4\x9a', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('bodydegree', models.IntegerField(default=3, verbose_name=b'\xe9\x86\x87\xe5\x8e\x9a\xe7\xad\x89\xe7\xb4\x9a', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('aftertastedegress', models.IntegerField(default=3, verbose_name=b'\xe5\xb0\xbe\xe9\x9f\xbb\xe7\xad\x89\xe7\xb4\x9a', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('balancedegress', models.IntegerField(default=3, verbose_name=b'\xe5\xb9\xb3\xe8\xa1\xa1\xe7\xad\x89\xe7\xb4\x9a', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('description', models.TextField(default=b'', verbose_name=b'\xe8\xa9\xb3\xe7\xb4\xb0\xe8\xaa\xaa\xe6\x98\x8e')),
                ('originitem', models.ForeignKey(to='bean.OriginItem')),
                ('roast', models.ForeignKey(to='bean.Roast')),
            ],
            options={
                'verbose_name': '\u70d8\u7119\u7119\u5ea6',
                'verbose_name_plural': '\u70d8\u7119\u7119\u5ea6',
            },
        ),
        migrations.AddField(
            model_name='originitem',
            name='park',
            field=models.ForeignKey(to='bean.Park'),
        ),
        migrations.AddField(
            model_name='originitem',
            name='process',
            field=models.ForeignKey(to='bean.Process'),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(to='bean.Region'),
        ),
    ]
