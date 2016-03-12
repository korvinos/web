# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    author = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.title

    def get_url(self):
        return '/question/%d/' % self.pk


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(null=True, blank=True)
    question = models.IntegerField(Question, null=True)
    author = models.ForeignKey(User, null=True)

    def get_url(self):
        return '/question/%d/' % self.question
