# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-30 02:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe7\x94\xa2\xe5\x93\x81\xe5\x90\x8d\xe7\xa8\xb1')),
                ('price', models.IntegerField(default=0, verbose_name=b'\xe7\x94\xa2\xe5\x93\x81\xe5\x83\xb9\xe6\xa0\xbc')),
                ('createdtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\xbb\xba\xe7\xab\x8b\xe6\x99\x82\xe9\x96\x93')),
            ],
            options={
                'verbose_name': '\u7522\u54c1\u9805\u76ee',
                'verbose_name_plural': '\u7522\u54c1\u9805\u76ee',
            },
        ),
        migrations.CreateModel(
            name='ProductPriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originprice', models.FloatField(default=0, verbose_name=b'\xe4\xb8\x8a\xe6\xac\xa1\xe9\x87\x91\xe9\xa1\x8d')),
                ('changedprice', models.FloatField(default=0, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe9\x87\x91\xe9\xa1\x8d')),
                ('createdtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\xbb\xba\xe7\xab\x8b\xe6\x99\x82\xe9\x96\x93')),
                ('productitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductItem')),
            ],
            options={
                'verbose_name': '\u7522\u54c1\u50f9\u683c\u8b8a\u52d5\u7d00\u9304',
                'verbose_name_plural': '\u7522\u54c1\u50f9\u683c\u8b8a\u52d5\u7d00\u9304',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe7\x94\xa2\xe5\x93\x81\xe9\xa1\x9e\xe5\x9e\x8b')),
            ],
            options={
                'verbose_name': '\u985e\u578b\u540d\u7a31',
                'verbose_name_plural': '\u985e\u578b\u540d\u7a31',
            },
        ),
        migrations.CreateModel(
            name='ProductUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa2\xe5\x93\x81\xe5\x96\xae\xe4\xbd\x8d')),
            ],
            options={
                'verbose_name': '\u55ae\u4f4d\u540d\u7a31',
                'verbose_name_plural': '\u55ae\u4f4d\u540d\u7a31',
            },
        ),
        migrations.AddField(
            model_name='productitem',
            name='producttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductType'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='productunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductUnit'),
        ),
    ]
