from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Shop, ShopASIC

# def ShopView(request, pk):
#     asics = Shop.objects.filter(user=pk)
#     return render(request, 'Shop.html', {"asics" : asics, "pk": pk, "name": "Shop"})


def ShopView(request, pk):
    shop = Shop.objects.get(user=pk)#Shop.objects.get(id=pk)
    print(shop.id)
    asics = ShopASIC.objects.filter(shop=shop.id) # Получаем все асики, связанные с магазином
    manufacturers = [asic.asic.manufacturer for asic in asics]
    if asics.first() is None:
        asics = None
    return render(request, 'Shop.html', {'asics': asics, 'manufacturers': manufacturers, "pk": pk, "name": "Shop"})

def ServiceView(request, pk):
    repairs = Service.objects.filter(user=pk)
    return render(request, 'Service.html', {"repairs" : repairs, "pk": pk, "name": "Service"})

def FarmView(request, pk):
    # asics = Farm.objects.filter(user=pk)
    return render(request, 'Farm.html', {"pk": pk, "name": "Farm"})

def HeatingView(request, pk):
    # asics = Shop.objects.filter(user=pk)
    return render(request, 'Heating.html', {"pk": pk, "name": "Heating"})

def ProductView(request):
    # asics = Shop.objects.filter(user=pk)
    return render(request, 'Product.html')


def ProductServiceView(request):
    # asics = Shop.objects.filter(user=pk)
    return render(request, 'ProductService.html')