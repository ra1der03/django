from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Article, Tag, Scope
from django import forms


class InlineFormset(forms.models.BaseInlineFormSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def clean(self):
        print(self.cleaned_data)
        for el in self.cleaned_data:
            if el.get('tag').is_main:
                self.count += 1
        if self.count > 1:
            raise ValidationError("Coudn't add two main tag for one elem")


class TagsInNews(admin.TabularInline):
    model = Scope
    extra = 2
    formset = InlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [TagsInNews]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_main']


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'article']

