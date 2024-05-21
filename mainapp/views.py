from django.shortcuts import render
from mainapp.models import Product

def index(request):
  product_list = Product.objects.all()
  
  context = {
    'products': product_list
  }

  return render(request, 'mainapp/index.html', context)
