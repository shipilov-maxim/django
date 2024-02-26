from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from pytils.translit import slugify
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Category, Blog


class HomePageView(TemplateView):
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Домашняя'
        return context


class ContactView(View):
    template_name = 'catalog/contact.html'

    def get(self, request):
        context = {'title': 'Контакты'}
        return render(request, self.template_name, context)

    def post(self, request):
        context = {'title': 'Отправлено!'}
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{email} - {message}')
        return render(request, self.template_name, context)


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'title': 'Каталог',
            'object_list': Product.objects.all()
        }
        return context


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'title': 'Категории',
            'object_list': Category.objects.all()
        }
        return context


class ProductDetailView(DetailView):
    model = Product


class CategoryDetailView(ListView):
    model = Category
    template_name = 'catalog/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        category = Category.objects.get(pk=pk)
        context = {
            'title': f'{category.name}',
            'object_list': Product.objects.filter(category=pk),
        }
        return context


class BlogDetailView(DetailView):
    model = Blog

    def get_absolute_url(self):
        return reverse('articles_detail', kwargs={'slug': self.slug})

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogListView(ListView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог'
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview')

    def get_success_url(self):
        return reverse('catalog:blog', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
