from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post, Author
from .filters import PostFilter


class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-dateCreation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    paginate_by = 10

    def get_queryset(self):
        # Получаем queryset объектов Post, отфильтрованных по postCategory = 'NW'
        queryset = Post.objects.filter(categoryType='NW').order_by(self.ordering)
        return queryset


class NewsSearch(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-dateCreation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    paginate_by = 10

    def get_queryset(self):
        # Получаем queryset объектов Post, отфильтрованных по postCategory = 'NW'
        queryset = Post.objects.filter(categoryType='NW').order_by(self.ordering)
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticlesList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        # Получаем queryset объектов Post, отфильтрованных по postCategory = 'NW'
        queryset = Post.objects.filter(categoryType='AR').order_by(self.ordering)
        return queryset


class ArticlesSearch(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        # Получаем queryset объектов Post, отфильтрованных по postCategory = 'NW'
        queryset = Post.objects.filter(categoryType='AR').order_by(self.ordering)
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'new'

    def get_object(self):
        obj = super().get_object()
        if obj.categoryType != 'NW':  # Проверяем, что это объект типа 'Статья'
            raise Http404("Новости с таким номером не существует.")
        return obj


class ArticleDetail(DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'article'

    def get_object(self):
        obj = super().get_object()
        if obj.categoryType != 'AR':  # Проверяем, что это объект типа 'Статья'
            raise Http404("Статьи с таким номером не существует.")
        return obj


class NewCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    # Класс для создания новой новости
    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'


    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        author, created = Author.objects.get_or_create(authorUser=self.request.user)
        post.author = author
        post.save()

        return super().form_valid(form)


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class NewEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'


class ArticleEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'


class NewDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'new_del.html'
    success_url = reverse_lazy('news_list')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'new_del.html'
    success_url = reverse_lazy('articles_list')
