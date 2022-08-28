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

#view to add user
def adduser(request):
    if request.method == 'GET':
        context={}
        return render(request, 'adduser.html', context)

#view to manage user
def manageuser(request):
    if request.method == 'GET':
        context  = {}
        return render(request, 'manageuser.html', context)
#view to add groups
def addgroups(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'addgroups.html', context)
#view to manage groups
def managegroups(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'managegroups.html', context)

#view to manage brands
def managebrands(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'managebrands.html', context)
#view to manage brands
def managecategory(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'managecategory.html', context)
#view to manage brands
def managestores(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'managestores.html', context)
#view to manage brands
def manageattr(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'manageattr.html', context)
#view to add new product
def addproduct(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'addprod.html', context)
#view to manage product
def manageproducts(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'manageproducts.html', context)
#view to add new order
def addorder(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'addorder.html', context)

#view to manage new order
def manageorder(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'manageorder.html', context)
#view for reports
def reports(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'reports.html', context)
#view for company
def company(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'company.html', context)
#view for profile
def profile(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'profile.html', context)
#view for profile
def settings(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'settings.html', context)

#view to manage
def logout(request):
    request.session.flush()
    return redirect('users:login')

