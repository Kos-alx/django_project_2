from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewEdit, NewCreate, NewDelete, NewDetail, ArticleCreate, ArticlesList, ArticleDetail, \
   ArticleEdit, ArticleDelete, NewsSearch, ArticlesSearch

urlpatterns = [

   path('news/', NewsList.as_view(), name='news_list'),
   path('news/search/', NewsSearch.as_view(), name='news_search'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('news/<int:pk>', NewDetail.as_view(), name='new_detail'),
   path('news/create/', NewCreate.as_view(), name='new_create'),
   path('news/<int:pk>/edit', NewEdit.as_view(), name='new_edit'),
   path('news/<int:pk>/delete', NewDelete.as_view(), name='new_delete'),

   path('articles/', ArticlesList.as_view(), name='articles_list'),
   path('articles/search/', ArticlesSearch.as_view(), name='articles_search'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('articles/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
   path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/edit', ArticleEdit.as_view(), name='article_edit'),
   path('articles/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),


]