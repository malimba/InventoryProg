from django.shortcuts import render, redirect, HttpResponse
from .models import Products
# Create your views here.

def Home(request):
    if request.method == 'GET':
        allProds = Products.objects.all()
        context = {'prods':allProds}
        return render(request, 'inventory.html', context)

def additems(request):
    if request.method == 'GET':
        return render(request, 'additem.html')
    if request.method == 'POST':
        print(request.POST)
        new_prod = Products.objects.create(product_name=str(request.POST['product_name']), units=int(request.POST['units']), price=float(request.POST['price']))
        new_prod.save()
        allProds = Products.objects.all()
        context = {'prods': allProds}
        return redirect('mainsite:Home')
def delete(request, prodid):
    if request.method == 'GET':
        itm = Products.objects.get(id=int(prodid))
        print(f'Deleting {itm}')
        itm.delete()
        return redirect('mainsite:Home')


