from django.shortcuts import render, redirect, HttpResponse
from .models import Products
import json
from users.models import User
# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
def Home(request):
    if request.method == 'GET':
        try:
            if not request.session['loggedin']:
                return redirect('users:login')
            allProds = Products.objects.all()
            context = {'prods':allProds, 'selected':request.session['selected']}
            return render(request, 'inventory.html', context)
        except Exception as e:
            print(e)
            try:
                if not request.session['loggedin']:
                    return redirect('users:login')
            except Exception:
                return redirect('users:login')
            allProds = Products.objects.all()
            context = {'prods':allProds}
            return render(request, 'inventory.html', context)
    if is_ajax(request) and request.method == "POST":

        successful_json_none = {'value':False}
        successful_json = {'value':True}
        if request.POST['type'] == 'selected':
            try:
                selected_itms = request.session['selected']
                selected_itms.append(int(request.POST['prodid']))
                request.session['selected'] = selected_itms
                print(selected_itms)
                return HttpResponse(json.dumps(successful_json))
            except Exception as e:
                print(e, 'here1')
                request.session['selected'] = list(request.POST['prodid'])
                return HttpResponse(json.dumps(successful_json))
        if request.POST['type'] == 'unselected':
            try:
                selected_itms = request.session['selected']
                selected_itms.pop(selected_itms.index(int(request.POST['prodid'])))
                request.session['selected'] = selected_itms
                print(selected_itms)
                return HttpResponse(json.dumps(successful_json))
            except Exception as e:
                print(e, 'here2')
                request.session['selected'] = []
                return HttpResponse(json.dumps(successful_json_none))

def additems(request):
    if request.method == 'GET':
        if not request.session['loggedin']:
            return redirect('users:lofin')
        return render(request, 'additem.html')
    if request.method == 'POST':
        if not request.session['loggedin']:
            return redirect('users:login')
        print(request.POST)
        new_prod = Products.objects.create(product_name=str(request.POST['product_name']), units=int(request.POST['units']), price=float(request.POST['price']))
        new_prod.save()
        allProds = Products.objects.all()
        context = {'prods': allProds}
        return redirect('mainsite:Home')
def delete(request, prodid):
    if request.method == 'GET':
        if not request.session['loggedin']:
            return redirect('users:login')
        itm = Products.objects.get(id=int(prodid))
        print(f'Deleting {itm}')
        itm.delete()
        return redirect('mainsite:Home')

def checkout(request):
    if request.method == 'GET':
        if not request.session['loggedin']:
            return redirect('users:login')
        allselecteditms = []
        for itm in request.session['selected']:
            allselecteditms.append(Products.objects.get(id=itm))
        context = {'selected':allselecteditms}
        return render(request, 'checkout.html', context)

def confirm(request):
    if request.method == 'POST':
        if not request.session['loggedin']:
            return redirect('users:login')
        print(request.POST)
        try:
            #start maniputtion of data
            #first do the subtraction
            for itm in request.session['selected']:
                if request.POST[f'{itm}']:
                    currentProd = Products.objects.get(id=int(itm))
                    currentProd.units = int(currentProd.units) - int(request.POST[f'{itm}'])
                    CurrentUser = User.objects.get(id=int(request.session['uid']))
                    amountMade = float(int(request.POST[f'{itm}']) * currentProd.price)
                    print(amountMade)
                    print(currentProd.amountmade)
                    currentProd.amountmade = float(currentProd.amountmade + amountMade)
                    # CurrentUser.save()

                    currentProd.save()
                if request.POST[f'{itm}c']:
                    # add prod units
                    currentProd = Products.objects.get(id=int(itm))
                    currentProd.units = int(currentProd.units) + int(request.POST[f'{itm}c'])
                    currentProd.save()
            #redirect back to inventory
            request.session['selected'] =[]
            return redirect('mainsite:Home')
        except Exception as e:
            print(e)

def logout(request):
    request.session.flush()
    return redirect('users:login')

