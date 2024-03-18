from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.get(email='admin@admin.com').delete()
        user = User.objects.create(
            email='admin@admin.com',
            first_name='Admin',
            last_name='Adminov',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('1234')
        user.save()
