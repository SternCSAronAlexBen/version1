# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='story',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('headline', models.CharField(max_length=50)),
                ('story', models.CharField(max_length=500)),
                ('time', models.CharField(max_length=50)),
            ],
        ),
    ]
