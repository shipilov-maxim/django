from pathlib import Path
import json

from django.core.management import BaseCommand

from catalog.models import Category, Product

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(BASE_DIR / 'fixture/data.json', encoding='UTF-8') as f:
            data = json.load(f)
            list_categories = []
            for obj in data:
                if obj['model'] == 'catalog.category':
                    list_categories.append(obj)
            return list_categories

    @staticmethod
    def json_read_products():
        with open(BASE_DIR / 'fixture/data.json', encoding='UTF-8') as f:
            data = json.load(f)
            list_products = []
            for obj in data:
                if obj['model'] == 'catalog.product':
                    list_products.append(obj)
            return list_products

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category['pk'], name=category['fields']['name'],
                         description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(pk=product['pk'],
                        name=product['fields']['name'],
                        description=product['fields']['description'],
                        preview=product['fields']['preview'],
                        price=product['fields']['price'],
                        category=Category.objects.get(pk=product['fields']['category']))
            )

        Product.objects.bulk_create(product_for_create)
