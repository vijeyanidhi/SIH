# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-18 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_resetdata_emailid'),
        ('report', '0002_auto_20200118_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportBasic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportKey', models.CharField(max_length=240, null=True)),
                ('reportValue', models.CharField(max_length=240, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportKey', models.CharField(max_length=240, null=True)),
                ('reportValue', models.CharField(max_length=240, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='reportstring',
            name='ident',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.LoginData'),
        ),
        migrations.AlterField(
            model_name='reportvalues',
            name='reportID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.ReportString'),
        ),
        migrations.AddField(
            model_name='reportlist',
            name='reportID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.ReportString'),
        ),
        migrations.AddField(
            model_name='reportbasic',
            name='reportID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.ReportString'),
        ),
    ]
