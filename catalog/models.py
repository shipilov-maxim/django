from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    # created_at = models.DateField(verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to='preview/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за штуку')
    created_at = models.DateField(auto_now=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now_add=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    preview = models.ImageField(upload_to='preview/', **NULLABLE, verbose_name='Изображение')
    created_at = models.DateField(auto_now=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.PositiveIntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return f'{self.title} {self.created_at}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
