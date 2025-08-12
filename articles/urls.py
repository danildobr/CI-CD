from django.urls import path

from articles.views import articles_list, cicd

urlpatterns = [
    path('', articles_list, name='articles'),
    path('cicd', cicd, name='cicd'),
]
