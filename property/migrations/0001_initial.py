# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-16 13:13
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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='properties/')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='CityImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='city/')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='properties/')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='MyProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='properties/')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Neighborhood',
                'verbose_name_plural': 'Neighborhoods',
            },
        ),
        migrations.CreateModel(
            name='NeighborhoodImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='neigborhood/')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('storey', models.CharField(blank=True, choices=[('Bungalow', 'Bungalow'), ('Duplex', 'Duplex'), ('One Storeys', 'One Storeys'), ('Two Storeys', 'Two Storeys'), ('Three Storeys', 'Three Storeys'), ('Four Storeys', 'Four Storeys'), ('Five Storeys', 'Five Storeys')], max_length=300, verbose_name='storey')),
                ('bedroom', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=300, verbose_name='bed')),
                ('bathroom', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=300, verbose_name='bathroom')),
                ('description', models.TextField()),
                ('furnished', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no'), ('somewhat', 'somewhat')], max_length=300, verbose_name='furnished')),
                ('parking_space', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=300, verbose_name='parking_space')),
                ('new_property', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=300, verbose_name='new_property')),
                ('purpose', models.CharField(blank=True, choices=[('Residential', 'Residential'), ('Office', 'Office'), ('Business', 'Business'), ('Other', 'Other')], max_length=300, verbose_name='purpose')),
                ('duration', models.CharField(blank=True, choices=[('1 month', '1 month'), ('3 months', '3 months'), ('6 months', '6 months'), ('Year', 'Year'), ('2 Years', '2 Years'), ('3 Years', '3 Years')], max_length=300, verbose_name='duration')),
                ('square_meter', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20)),
                ('price', models.DecimalField(decimal_places=0, default=0.0, max_digits=20)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='properties/')),
                ('main_image_two', models.ImageField(blank=True, null=True, upload_to='properties/')),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default='', max_length=300, on_delete=django.db.models.deletion.CASCADE, to='property.Category')),
                ('city', models.ForeignKey(blank=True, default='', max_length=300, on_delete=django.db.models.deletion.CASCADE, to='property.City')),
                ('neighborhood', models.ForeignKey(blank=True, default='', max_length=300, on_delete=django.db.models.deletion.CASCADE, to='property.Neighborhood')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Property',
            },
        ),
        migrations.CreateModel(
            name='PropertyRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
