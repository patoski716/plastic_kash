from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .forms import *
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject,phone=phone, message=message)

        contact.save()
        messages.success(request, 'Your message was sent successfully, We will get back to you soon')
    return render(request,'contact.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('vendor')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, f'You are now registered as {username} and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'register.html')


@login_required(login_url='login')
def vendor(request):
    form = VendorForm()
    if request.method == 'POST':
        form = VendorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/')
    context={'form':form}
    return render(request,'vendor.html',context)

@login_required(login_url='login')
def dashboard(request):
    count=Product.objects.filter(user_id=request.user.id).count()
    # user_products = Product.objects.order_by('-created_date').filter(user_id=request.user.id)

    context = {'count':count}
    return render(request,'dashboard/dashboard.html',context)



