from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField


class WordsSet(models.Model):
    title = models.CharField(max_length=64, unique=False, null=False, verbose_name='Title')
    slug = AutoSlugField(populate_from='title', unique=False, null=False, verbose_name='word set slug')

    creator = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, verbose_name='Creator')

    def __str__(self):
        return f'{self.title} | from {self.creator}'

    class Meta:
        verbose_name = 'Word set'
        verbose_name_plural = 'Word sets'


class Words(models.Model):
    word = models.CharField(max_length=20, unique=False, null=False, verbose_name='Word')
    translation = models.CharField(max_length=20, unique=False, null=False, verbose_name='Translation')

    word_set = models.ForeignKey(WordsSet, on_delete=models.CASCADE, verbose_name='Word set')

    def __str__(self):
        return f'{self.word} | {self.translation}'

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'
