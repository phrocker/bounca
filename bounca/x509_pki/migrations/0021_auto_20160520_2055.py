# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('x509_pki', '0020_auto_20160518_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distinguishedname',
            old_name='subjectAltName',
            new_name='subjectAltNames',
        ),
    ]