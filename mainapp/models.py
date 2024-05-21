from django.db import models
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
  name = models.CharField(max_length=150, verbose_name="Name")
  image = models.ImageField(blank=True, upload_to='products')
  short_name = models.CharField(max_length=150, verbose_name="Short_name", default="")
  short_desc = models.CharField(max_length=250, blank=True)
  description = models.TextField(verbose_name="description")
  price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="price", default=0)
  quantity = models.PositiveIntegerField(default=0, verbose_name="quantity")
  def __str__(self):
    return self.name
  