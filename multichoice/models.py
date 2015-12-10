# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.db import models
from django.db.models import Q
from quiz.models import Question, Quiz


ANSWER_ORDER_OPTIONS = (
    ('content', _('Content')),
    ('random', _('Random')),
    ('none', _('None'))
)


class MCQuestion(Question):

    answer_order = models.CharField(
        max_length=30, null=True, blank=True,
        choices=ANSWER_ORDER_OPTIONS,
        help_text=_("The order in which multichoice "
                    "answer options are displayed "
                    "to the user"),
        verbose_name=_("Answer Order"))

    def check_if_correct(self, guess):
        answer = Answer.objects.get(id=guess)

        if answer.correct is True:
            return True
        else:
            return False

    def order_answers(self, queryset):
        if self.answer_order == 'content':
            return queryset.order_by('content')
        if self.answer_order == 'random':
            return queryset.order_by('?')
        if self.answer_order == 'none':
            return queryset.order_by()
        return queryset

    def get_answers(self):
        return self.order_answers(Answer.objects.filter(question=self))


    def get_answers_by_gender(self, gender):
        queryset = Answer.objects.filter(question=self)
        if gender:
            queryset = queryset.filter(Q(gender=gender) | Q(gender=Answer.GENDER_CHOICES[0][0]))
        return self.order_answers(queryset)

    def get_answers_list(self):
        return [(answer.id, answer.content) for answer in
                self.order_answers(Answer.objects.filter(question=self))]

    def answer_choice_to_string(self, guess):
        return Answer.objects.get(id=guess).content

    def get_answer_by_index(self, index):
        answers = Answer.objects.filter(question=self)
        if index < len(answers):
            return answers[index]
        return False

    def get_answer_by_index_v2(self, index):
        answer = Answer.objects.filter(question=self, index=index).first()
        
        return answer or False
        

    class Meta:
        verbose_name = _("Multiple Choice Question")
        verbose_name_plural = _("Multiple Choice Questions")


@python_2_unicode_compatible
class Answer(models.Model):
    GENDER_CHOICES = (
        ('0', 'Male and Male'),
        ('1', 'Male'),
        ('2', 'Female'),
    )
    question = models.ForeignKey(MCQuestion, verbose_name=_("Question"))

    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text=_("Enter the answer text that "
                                           "you want displayed"),
                               verbose_name=_("Content"))

    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text=_("Is this a correct answer?"),
                                  verbose_name=_("Correct"))

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="0")

    next_question = models.ForeignKey(MCQuestion, 
                                related_name="next_question_mcquestion_fk",
                                verbose_name=_("Next Question"), null=True, blank=True)
    next_quiz = models.ForeignKey(Quiz, 
                                related_name="next_quiz_mcquestion_fk",
                                verbose_name=_("Next Quiz"), null=True, blank=True)
    index = models.IntegerField(verbose_name=_("index alternative"), default=0)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["pk"]
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")  
