from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from myapp.forms import OrderForm, RegistrationForm, InterestForm
from datetime import datetime
from myapp.models import Category, Product, Client, Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import DetailView
from django.views.generic import ListView


class IndexView(ListView):
    model = Category

   # request.COOKIES['about_visits'] = no_of_visit
    #if 'last_login' in request.session:
        #last_log = request.session.get('last_login')
    #else:
     #   last_log = "Your last login was more than one hour ago"

   # product_list = Product.objects.all().order_by('price')[:5]
    #response = HttpResponse()
    #heading1 = '<p><center>' + 'List of categories: ' + '</center></p>'
    #response.write(heading1)
    #   para = '<p>' + str(category.id) + ': ' + str(category) + '</p>'
     #   response.write(para)
    #heading2 = '<p><center>' + 'List of Products: ' + '</center></p>'
    #response.write(heading2)
    #for product in product_list[::-1]:
     #   pro = '<p>' + str(product.name) + ': ' + str(product.price) + '</p>'
      #  response.write(pro)



  #  return render(request, 'myapp/index.html', {'cat_list': cat_list, 'last_log': last_log})



def about(request):
    #response = HttpResponse()
    #text = '<p>This is an Online Store App</p>'
    #response.write(text)


    if 'about_visits' in request.COOKIES:
        no_of_visit = request.COOKIES['about_visits']
        no_of_visit = no_of_visit + 1
        request.COOKIES['about_visits'] = no_of_visit
    else:
        request.COOKIES['about_visits'] = 1
    return render(request, 'myapp/about.html', {'no_of_visit':request.COOKIES['about_visits']})


def detail(request, cat_no):
    response = HttpResponse()
    details = get_object_or_404(Category, id=cat_no)
    text1 = '<p>'+str(details.name)+': ' + str(details.warehouse)+'</p>'
    response.write(text1)
    product_details = Product.objects.filter(category_id=cat_no)
   # for product in product_details:
       # pro = '<p>' + str(product.name) + ': ' + str(product.price) + '</p>'
      #  response.write(pro)
    return render(request, 'myapp/detail.html', {'details': details, 'product_details': product_details})


def products(request):
    prodlist = Product.objects.all().order_by('id')[:10]
    return render(request, 'myapp/products.html', {'prodlist': prodlist})


def place_order(request):
    msg = ''
    prodlist = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.num_units <= order.product.stock:
                order.save()
                msg = 'Order placed succesfully.'
            else:
                msg = 'We dont have sufficient stock to fill your order.'
            return render(request, 'myapp/order_response.html' , {'msg':msg})
    else:
        form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form':form, 'msg':msg, 'prodlist':prodlist})


def productdetail(request, prod_id):
    product = Product.objects.get(pk=prod_id)
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            data = form.data
            print('Interested:', data.get('interested'), data.get('quantity'))
            if data.get('interested') == '1':
                print('ProductInt', product.intrested)
                product.intrested = product.intrested + 1
            product.save()
        return redirect('myapp:index')
    else:
        form = InterestForm()
    return render(request, 'myapp/productdetail.html', {'form':form, 'product':product})
    # return render(request, 'myapp/productdetail.html', {'product':product})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                current_login_time = str(datetime.now())
                # session parameter last_login
                request.session['last_login'] = current_login_time
                request.session.set_expiry(3600)
                request.session['username'] = username
                # set session expiry to 1 hour
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myapp:login'))
    else:
        form = RegistrationForm()
    return render(request,'myapp/register.html', {'form': form})

@login_required(login_url="myapp/login/")
def myorders(request):
    if request.session.has_key('username'):
        username = request.session['username']
        client = Client.objects.filter(first_name__contains=username)
        order = Order.objects.filter(id=client.id)
        return render(request, 'myapp:my_order', {'order': order})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))