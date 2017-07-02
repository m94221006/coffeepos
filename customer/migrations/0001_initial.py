# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-06-20 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('phone', models.CharField(max_length=50, verbose_name=b'\xe9\x9b\xbb\xe8\xa9\xb1')),
                ('email', models.CharField(max_length=50, verbose_name=b'\xe9\x9b\xbb\xe5\xad\x90\xe9\x83\xb5\xe4\xbb\xb6')),
                ('createdtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\xbb\xba\xe7\xab\x8b\xe6\x99\x82\xe9\x96\x93')),
            ],
            options={
                'verbose_name': '\u5ba2\u6236\u5217\u8868',
                'verbose_name_plural': '\u5ba2\u6236\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='CustomerCardSaveHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savemoney', models.FloatField(default=0, verbose_name=b'\xe9\x87\x91\xe9\xa1\x8d')),
                ('createdtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\xbb\xba\xe7\xab\x8b\xe6\x99\x82\xe9\x96\x93')),
            ],
            options={
                'verbose_name': '\u5ba2\u6236\u5132\u503c\u7d00\u9304',
                'verbose_name_plural': '\u5ba2\u6236\u5132\u503c\u7d00\u9304',
            },
        ),
        migrations.CreateModel(
            name='CustomerMoneyCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savemoney', models.FloatField(default=0, verbose_name=b'\xe9\x87\x91\xe9\xa1\x8d')),
                ('createdtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\xbb\xba\xe7\xab\x8b\xe6\x99\x82\xe9\x96\x93')),
                ('lastupdatedtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x9c\x80\xe5\xbe\x8c\xe6\x9b\xb4\xe6\x96\xb0\xe6\x99\x82\xe9\x96\x93')),
            ],
            options={
                'verbose_name': '\u5ba2\u6236\u5132\u503c\u5217\u8868',
                'verbose_name_plural': '\u5ba2\u6236\u5132\u503c\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='MoneyCardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe9\xa1\x9e\xe5\x9e\x8b\xe5\x90\x8d\xe7\xa8\xb1')),
            ],
            options={
                'verbose_name': '\u5132\u503c\u5361\u985e\u578b',
                'verbose_name_plural': '\u5132\u503c\u5361\u985e\u578b',
            },
        ),
        migrations.AddField(
            model_name='customermoneycard',
            name='cardtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.MoneyCardType'),
        ),
        migrations.AddField(
            model_name='customermoneycard',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer'),
        ),
        migrations.AddField(
            model_name='customercardsavehistory',
            name='customercard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerMoneyCard'),
        ),
    ]