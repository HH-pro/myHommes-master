# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-12-08 11:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realtor', '0001_initial'),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='city',
        ),
        migrations.RemoveField(
            model_name='property',
            name='neighborhood',
        ),
        migrations.AddField(
            model_name='cityimage',
            name='city',
            field=models.ForeignKey(default='name', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='property.City'),
        ),
        migrations.AddField(
            model_name='images',
            name='property',
            field=models.ForeignKey(default='hellok', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='property.Property'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myproperty',
            name='property',
            field=models.ManyToManyField(blank=True, to='property.Property'),
        ),
        migrations.AddField(
            model_name='myproperty',
            name='user',
            field=models.OneToOneField(default='name', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='city',
            field=models.ForeignKey(blank=True, default=1, max_length=300, on_delete=django.db.models.deletion.CASCADE, to='property.City'),
        ),
        migrations.AddField(
            model_name='neighborhoodimage',
            name='neighborhood',
            field=models.ForeignKey(default='hello', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='property.Neighborhood'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='realtor',
            field=models.ForeignKey(default='hi', on_delete=django.db.models.deletion.CASCADE, to='realtor.Realtor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.ImageField(blank=True, default='city', null=True, upload_to='properties/'),
        ),
    ]
