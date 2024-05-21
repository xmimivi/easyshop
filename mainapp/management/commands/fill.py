from typing import Any
from django.core.management import BaseCommand
from mainapp.models import Product
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from authapp.models import ShopUser

class Command(BaseCommand):

  def handle(self, *args, **options):
     super_user = ShopUser.objects.create_superuser('root','django@geekshop.local', 'root')