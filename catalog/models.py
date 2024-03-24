from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

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
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                verbose_name='Создатель', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('set_published', 'Can publish posts'),
            ('change_description', 'Can change description'),
            ('change_category', 'Can change category')
        ]


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    preview = models.ImageField(upload_to='preview/', **NULLABLE, verbose_name='Изображение')
    created_at = models.DateField(auto_now=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.PositiveIntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_title = models.CharField(max_length=100, verbose_name='Название версии')
    is_actual_version = models.BooleanField(verbose_name='Признак актуальной версии', default=False)

    def __str__(self):
        return f'{self.version_title}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
