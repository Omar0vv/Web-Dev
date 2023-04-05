from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.http.response import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse('Check')



def cats_list(request):
    cats = Category.objects.all()
    cats_json = [cat.to_json() for cat in cats]
    return JsonResponse(cats_json, safe=False)


def about_cat(request, id):
    try:
        cat = Category.objects.get(id=id).to_json()
        return JsonResponse(cat)
    except Category.DoesNotExist as cdne:
        return JsonResponse({'message': str(cdne)}, status=400)
    

def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def about_product(request, id):
    try:
        product = Product.objects.get(id=id)
        return JsonResponse(product.to_json())
    except Product.DoesNotExist as pdne:
        return JsonResponse({'message': str(pdne)}, status=400)
    