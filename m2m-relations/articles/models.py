import re

from django.db import models


class Tag(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='tag_id')
    name = models.CharField(max_length=30, verbose_name='Тег')
    is_main = models.BooleanField(verbose_name='is_main')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        constraints = [models.UniqueConstraint(fields=['is_main', 'name'], name='main')]

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='article_id')
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Tag, related_name='scopes', through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-published_at',)

    def __str__(self):
        return self.title


class Scope(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='merge_id')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Связка'
        verbose_name_plural = 'Связки'
        constraints = [models.UniqueConstraint(fields=['tag', 'article'], name='tags')]

    def __str__(self):
        return self.tag.name
