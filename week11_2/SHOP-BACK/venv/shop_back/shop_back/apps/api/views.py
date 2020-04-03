from django.shortcuts import render
from . models import Category, Product
from django.http import Http404, HttpResponseRedirect


def index(request):
    return render(request,'api/index.html')


def categories(request):
    category_list = Category.objects.order_by('id')
    return render(request, 'api/category_list.html', {'category_list': category_list})

def detail(request, category_id):
    try:
        c = Category.objects.get(id = category_id)
    except:
        raise Http404("Not found!")
    return render(request,'api/category_details.html', {'category':c})

def products(request, category_id):
    try:
        product_list = Product.objects.filter(category_id = category_id)
    except:
        raise Http404("Not found!")
    return render(request,'api/product_list.html', {'product_list':product_list})

def product_detail(request, product_id):
    try:
        p = Product.objects.get(id = product_id)
    except:
        raise Http404("Not found!")
    return render(request, 'api/product_details.html',{'product' : p})