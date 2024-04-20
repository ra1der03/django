from django.contrib import admin
from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, forms


class ScopeInlineFormset(BaseInlineFormSet):
    class Meta:
        model = Scope
# переопределению форм в лекции, к сожалению, внимания не уделили нисколько и соответственно, без
# знаний об этом часть задания, касающуюся проверки главного тега, выполнить не удается. В остальном все в порядке
    def save(self, *args, **kwargs):
        data = args
        if (i.is_main == "True" for i in data.scopes.all()) and (el.is_main == "True" for el in Scope.objects.all()):
            raise forms.ValidationError('Главным может быть лишь один заголовок')
        return super().clean()


class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 2


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [ScopeInLine]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_main']


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'article']

