from django.shortcuts import render,HttpResponse,redirect
from ecommerceadmin.models import *
from . models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.conf import settings

import stripe
stripe.api_key = "sk_test_51LONVLSGiIV6e8axvTlBBRP1GkLUEp7IlyGF00Ec0QvMf63FvQoydtHL0AZ7McoUMzN4mFIRlhKZ6XKGNrNNEnET001hYYRZkJ"

def index(request):
    allproducts = product.objects.all()
    print(allproducts)
    return render(request,'index.html',{'allproducts':allproducts})
def register(request):
    if request.method == 'POST':
        usernames = request.POST['usernames']
        email = request.POST['email']
        passwords = request.POST['passwords']
        print(usernames,passwords)
        User.objects.create_user(username=usernames,password=passwords,email=email)

        return redirect('index')
    else:
        return render(request,'register.html')

def authlogin(request):
    if request.method == 'POST':
        usernames = request.POST['usernames']
        passwords = request.POST['passwords']
        print(usernames,passwords)
        user = authenticate(request, username=usernames, password=passwords)
        login(request,user)
        return redirect('index')
            # return redirect('authenticate')
    else:
        return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return  redirect('index')

@login_required(login_url='/authlogin')
def purchase(request,id):
    productid = product.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        purchasesave = buy(
            name = name,
            phone = phone,
            address = address,
            productid = productid,
            userid = request.user,
        )
        purchasesave.save()
        return redirect('payment')
    else:
        return render(request,'buy.html',{'id':id,'productid':productid})

def itemdetail(request,id):
    item = product.objects.get(id=id)
    return render(request,'itemdetail.html',{'item':item})

def orders(request):
    id = request.user.id
    print(id)
    order = buy.objects.filter(productid=id)
    print(order)
    return render(request,'orders.html',{'order':order})

def rating(request,id):
    products = product.objects.get(id=id)
    if request.method == 'POST':
        stars = request.POST['rating']
        title = request.POST['title']
        description = request.POST['reviews']
        ratesave = Rating(
            products = products,
            givenby = request.user,
            stars = stars,
            title = title,
            description = description,
        )
        ratesave.save()
        return HttpResponse('reviewss done')
    else:
        return render(request,'reviews.html',{'id':id})

#######Payment Integration in Stripe

def payment(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        name = request.user.username
        print(name)

        customer = stripe.Customer.create(
            name=name,

            source=request.POST['stripeToken']
        )

        stripe.PaymentIntent.create(
            customer=customer,
            amount=1059,
            currency="usd",
            description="Software development services by shiv",
        )

        return render(request,'success.html')
    else:
        return render(request,'home.html',{'key':key})
