from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    list_ = Article.objects.all().order_by('-published_at')
    context = {'articles': list_}
    return render(request, template, context)
