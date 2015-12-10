# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multichoice', '0002_auto_20151204_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='gender',
            field=models.CharField(default='0', max_length=1, choices=[('0', 'Male and Male'), ('1', 'Male'), ('2', 'Female')]),
        ),
    ]
