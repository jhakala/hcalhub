# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignee',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='assignee',
            name='issues',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='issues.Issue'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='close_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date closed'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_assignee',
            field=models.CharField(default='unassigned', max_length=50),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_category',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_comment',
            field=models.CharField(default='', max_length=20000),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_dump',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_status',
            field=models.CharField(default='', max_length=30),
        ),
    ]
