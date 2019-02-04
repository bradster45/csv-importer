# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=256, unique=True)
    legacy_id = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    def __str__(self, ):
        return self.title


class Page(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name="pages")
    content = models.TextField()
    number = models.PositiveIntegerField()

    def __str__(self, ):
        return "{} page {}".format(self.article.title, self.number)
