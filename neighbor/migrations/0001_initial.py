# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-05 15:13
from __future__ import unicode_literals

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
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='business/')),
                ('project', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Neighborhood', models.CharField(max_length=30, null=True)),
                ('Neighborhood_location', models.CharField(max_length=30, null=True)),
                ('population', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('image_name', models.CharField(max_length=30)),
                ('message', models.TextField(blank=True, max_length=100, null=True)),
                ('estate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbor.Neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default='bio please...', max_length=100)),
                ('profilepic', models.ImageField(blank=True, default='../static/images/bad-profile-pic-2.jpeg', upload_to='profile/')),
                ('email', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbor.Profile'),
        ),
        migrations.AddField(
            model_name='follow',
            name='estate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbor.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='business',
            name='estate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbor.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
