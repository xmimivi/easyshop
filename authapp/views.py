from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegistrForm
from django.contrib import auth
from django.urls import reverse


def login(request):
  title = "login"

  login_form = ShopUserLoginForm(data=request.POST)
  if request.method == 'POST' and login_form.is_valid():
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user and user.is_active:
      auth.login(request, user)
      return HttpResponseRedirect(reverse('main'))
    
  content = {'title': title, 'login_form':login_form}
  return render(request, 'authapp/login.html', content)

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect(reverse('main'))

def register(request):
  title = 'Регистрация'

  if request.method == "POST":
    register_form = ShopUserRegistrForm(request.POST, request.FILES)

    if register_form.is_valid():
      register_form.save()
      return HttpResponseRedirect(reverse('authapp:login'))
  else:
    register_form = ShopUserRegistrForm()
  context = {
    'title':title,
    'register_form': register_form
  }

  return render(request, 'authapp/register.html', context)

def edit(request):
  return HttpResponseRedirect(reverse('main'))
