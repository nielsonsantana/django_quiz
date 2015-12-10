# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '__first__'),
        ('multichoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='index',
            field=models.IntegerField(default=0, verbose_name='Id fixo alternativa'),
        ),
        migrations.AddField(
            model_name='answer',
            name='next_question',
            field=models.ForeignKey(related_name='next_question_mcquestion_fk', verbose_name='Next Question', blank=True, to='multichoice.MCQuestion', null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='next_quiz',
            field=models.ForeignKey(related_name='next_quiz_mcquestion_fk', verbose_name='Next Quiz', blank=True, to='quiz.Quiz', null=True),
        ),
    ]
