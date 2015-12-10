# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multichoice', '0003_answer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='index',
            field=models.IntegerField(default=0, verbose_name='index alternative'),
        ),
    ]
