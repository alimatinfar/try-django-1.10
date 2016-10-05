# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 20:07
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/%Y-%m-%d', verbose_name='main image')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content')),
                ('updateDateTime', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('createDateTime', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
        ),
    ]