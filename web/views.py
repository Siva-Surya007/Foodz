from django.shortcuts import render, reverse

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from users.models import User 
from customer.models import Customer
from restaurent.models import *


@login_required(login_url='/login/')
def index(request):
    store_categories =  StoreCategory.objects.all()
    sliders = Slider.objects.all()
    stores = Store.objects.all()
    context = {
        "store_categories" : store_categories,
        "stores" : stores,
        'sliders' : sliders
    } 
    return render(request,'web/index.html',context=context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            context = {
                'error' : True,
                'message' : 'Invalid email or password'
            }
            return render(request,'web/login.html',context=context)

    else:
        return render(request,'web/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            context = {
                'error' : True,
                'message' : 'Email already exists'
            }

            return render(request,'web/register.html',context=context)
        
        else:

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                is_customer = True
                )
            user.save()

            customer = Customer.objects.create(user=user)
            customer.save()
            return HttpResponseRedirect(reverse('web:login'))
        
    else:
        return render(request,'web/register.html')
    

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('web:login'))



@login_required(login_url='/login/')
def restaurents(request,id):

    store_categories =  StoreCategory.objects.all()
    stores = Store.objects.all()

    selected_category = StoreCategory.objects.get(id=id)

    stores = stores.filter(category = selected_category)
    
    context = {
        "store_categories" : store_categories,
        "stores" : stores
    } 
    
    return render(request,'web/restaurents.html',context=context)




def restaurent(request,id):
    restaurent = Store.objects.get(id=id)
    food_category = FoodCategory.objects.filter(store = restaurent)


    context = {
        'food_category' : food_category,
        'restaurent' : restaurent
    }

    return render(request,'web/restaurent.html',context=context)



@login_required(login_url='/login/')
def cart(request):
    return render(request,'web/cart.html')
