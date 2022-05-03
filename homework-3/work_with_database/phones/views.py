from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    if request.GET.get('sort') == 'min_price':
        phone_objects = Phone.objects.order_by('price')

    elif request.GET.get('sort') == 'max_price':
        phone_objects = Phone.objects.order_by('-price')

    else:
        phone_objects = Phone.objects.order_by('name')

    context = {
        'phones': phone_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone_objects = Phone.objects.get(slug=slug)
    except:
        phone_objects = None
    context = {
        'phone': phone_objects
    }
    return render(request, template, context)
