from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.order_by('-published_at')
    context = {'object_list': articles}
    return render(request, template, context)

def cicd(request):
    current_time = 'сегодня'
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)