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
    # category = models.CharField(max_length=100, verbose_name='Категория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за штуку')
    created_at = models.DateField(**NULLABLE, verbose_name='Дата создания')
    updated_at = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')
    # manufactured_at = models.DateField(**NULLABLE, verbose_name='Дата производства')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
