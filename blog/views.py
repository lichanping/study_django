from django.shortcuts import render
from django.http import HttpResponse

from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == "0":
        return render(request, 'edit_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})
