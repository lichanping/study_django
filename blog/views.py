from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):
    article_val = models.Article.objects.get(pk=1)
    return render(request, 'index.html', {'article': article_val})
