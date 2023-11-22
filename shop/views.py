from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib import messages
from shop.forms import CustomUserForm
import jazzmin
import json
from django.http import JsonResponse


def home(request):
    products = Product.objects.filter(trending=1)
    return render(request, "shop/index.html", {'products':products})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "logged out succesfully")
    return redirect('/')

def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request, "shop/cart.html", {'cart':cart})
    else:
        return redirect('/')

def remove_cart(request,cid):
    cart_item=Cart.objects.get(id=cid)
    cart_item.delete()
    return redirect('cart')

def remove_fav(request,fid):
    fav_item=Favourite.objects.get(id=fid)
    fav_item.delete()
    return redirect('/favviewpage')

def fav_page(request):
    if request.headers.get('x-requested-with')==('XMLHttpRequest'):
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            product_status = Product.objects.get(id=product_id)
            if product_status:
                if Favourite.objects.filter(user = request.user.id, product_id=product_id):
                    return JsonResponse({'status':'product already in Favourite'},status=200)
                else:
                    Favourite.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':'product added to favourite '},status=200)
        else:
            return JsonResponse({'status':'login to add favorite'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def favviewpage(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request, "shop/fav.html", {'fav':fav})
    else:
        return redirect('/')

def add_to_cart(request):
    if request.headers.get('x-requested-with')==('XMLHttpRequest'):
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            #print(request.user.id)
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id, product_id=product_id):
                    return JsonResponse({'status':'product already added to cart'},status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'product added  to cart '},status=200)
                    else:
                        return JsonResponse({'status':'product stock not available'},status=200)
        else:
            return JsonResponse({'status':'login to add cart'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
    

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=username, password=pwd)
            if user is not None:
                messages.success(request, "Logged in successfully")
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
                return redirect('/login')
        return render(request, 'shop/login.html')

def register(request):
    form = CustomUserForm()
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration successfully you can login now")
            return redirect("/login")

    return render(request, "shop/register.html", {"form":form})


def collections(request):
    category = Category.objects.filter(status=0)
    return render(request, "shop/collections.html",{"category":category})

def collectionsview(request, name):
    if(Category.objects.filter(name=name,status = 0)):
        products = Product.objects.filter(category__name=name)
        return render(request, "shop/products/index.html", {"products":products, "category_name":name})
    else:
        messages.WARNING(request,"this catetogry name not available")
        return redirect('collections')

def product_details(request, cname, pname):
    if(Category.objects.filter(name=cname, status=0)):
        if(Product.objects.filter(name=pname, status=0)):
            product = Product.objects.filter(name=pname, status=0).first()
            return render(request, "shop/products/product_detail.html", {"products":product})
        else:
            messages.error(request, "no such product found ")
    else:
        messages.error(request, "no such category found ")
    

