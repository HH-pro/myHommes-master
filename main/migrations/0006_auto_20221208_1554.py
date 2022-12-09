# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-12-08 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20221208_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='Documents',
            new_name='Bank_Statement',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='Your_Name',
            new_name='Your_Email_Address',
        ),
        migrations.AddField(
            model_name='form',
            name='Contract',
            field=models.FileField(default='yes', upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='Guarantor_contract',
            field=models.FileField(default='yess', upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='Proof_of_Address',
            field=models.FileField(default='k', upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='Proof_of_ID',
            field=models.FileField(default='q', upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='Work_payslip',
            field=models.FileField(default='q', upload_to='documents/'),
            preserve_default=False,
        ),
    ]
