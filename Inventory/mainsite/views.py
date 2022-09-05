from django.shortcuts import render, redirect, HttpResponse
from .models import *
import json
from users.models import *
from datetime import datetime
# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
def Home(request):
    if request.method == 'GET':
        try:
            if not request.session['loggedin']:
                return redirect('users:login')
            allProds = Products.objects.all()
            prod_no = len(allProds)
            allOrders =   Order.objects.all()
            order_no = len(allOrders)
            allUsr = User.objects.all()
            usr_no = len(allUsr)
            allStores = Stores.objects.all()
            store_no = len(allStores)
            context = {'prods':allProds, 'prod_no':prod_no, 'selected':request.session['selected'], 'order_no':order_no, 'usr_no':usr_no, 'store_no':store_no}
            return render(request, 'inventory.html', context)
        except Exception as e:
            print(e)
            try:
                if not request.session['loggedin']:
                    return redirect('users:login')
            except Exception:
                return redirect('users:login')
            allProds = Products.objects.all()
            prod_no = len(allProds)
            allOrders = Order.objects.all()
            order_no = len(allOrders)
            allUsr = User.objects.all()
            usr_no = len(allUsr)
            allStores = Stores.objects.all()
            store_no = len(allStores)
            context = {'prods':allProds, 'prod_no':prod_no, 'order_no':order_no, 'usr_no':usr_no, 'store_no':store_no}
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
        #retrieve groups
        allGroups = Groups.objects.all()
        context={'groups':allGroups}
        return render(request, 'adduser.html', context)
    if is_ajax(request) and request.method == 'POST':
        print(request.POST)

#view to manage user
def manageuser(request):
    if request.method == 'GET':
        users = User.objects.all()
        total_entries = len(users)
        context  = {'allusers':users, 'totalentries':total_entries}
        return render(request, 'manageuser.html', context)
#view to add groups
def addgroups(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'addgroups.html', context)
    if is_ajax(request) and request.method =='POST':
        successful_json = {'value':True}
        unsuccessful_json = {'value':False}
        try:
            # print(request.POST)
            newGroup = Groups.objects.create(group_name=request.POST['groupname'], permissions=request.POST['selectedPerm'])
            newGroup.save()
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps(unsuccessful_json))

    # if request.method == ''
#view to manage groups
def managegroups(request):
    if request.method == 'GET':
        allGroups = Groups.objects.all()
        context = {'allgroups':allGroups, 'totalentries':len(allGroups)}
        return render(request, 'managegroups.html', context)


#view to manage brands
def managebrands(request):
    if request.method == 'GET':
        allBrands = Brand.objects.all()
        context = {'allBrands':allBrands}
        return render(request, 'managebrands.html', context)
    if request.method == 'POST':
        brandname = request.POST['brandname']
        status = request.POST['status']
        newBrandObj = Brand.objects.create(brand_name=brandname, status=status)
        newBrandObj.save()
        return redirect('mainsite:managebrands')
def removebrand(request):
    if request.method == 'POST':
        try:
            print(request.POST['brandid'])
            brandid = int(request.POST['brandid'])
            brandObj = Brand.objects.get(id=int(brandid))
            brandObj.delete()
            successful_json = {'success':True, 'message':'Success'}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'value': False}
            return HttpResponse(json.dumps(unsuccessful_json))
def removeproduct(request):
    if request.method == 'POST':
        try:
            print(request.POST['product_id'])
            productid = int(request.POST['product_id'])
            productObj = Products.objects.get(id=int(productid))
            productObj.delete()
            successful_json = {'success':True, 'message':'Success'}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'value': False}
            return HttpResponse(json.dumps(unsuccessful_json))
def removestore(request):
    if request.method == 'POST':
        try:
            print(request.POST['store_id'])
            storeid = int(request.POST['store_id'])
            storeObj = Stores.objects.get(id=int(storeid))
            storeObj.delete()
            successful_json = {'success':True, 'message':'Success'}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'value': False}
            return HttpResponse(json.dumps(unsuccessful_json))
def removeCategory(request):
    if request.method == 'POST':
        try:
            print(request.POST['category_id'])
            categoryid = int(request.POST['category_id'])
            categoryObj = Category.objects.get(id=int(categoryid))
            categoryObj.delete()
            successful_json = {'success':True, 'message':'Success'}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'value': False}
            return HttpResponse(json.dumps(unsuccessful_json))
def removeAttr(request):
    if request.method == 'POST':
        try:
            print(request.POST['attrid'])
            attrid = int(request.POST['attrid'])
            attrObj = Attribute.objects.get(id=int(attrid))
            attrObj.delete()
            successful_json = {'success':True, 'messages':'Success'}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'value': False}
            return HttpResponse(json.dumps(unsuccessful_json))
def fetchBrandData(request):
    if request.method == 'POST':
        try:
            brandid = int(request.POST['brandid'])
            brandObj = Brand.objects.get(id=int(brandid))
            successful_json = {'name':brandObj.brand_name, 'status':brandObj.status}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'success':False, 'message':'Server side error'}
            return HttpResponse(json.dumps(unsuccessful_json))
def fetchCategoryData(request):
    if request.method == 'POST':
        try:
            catid = int(request.POST['categoryid'])
            categoryObj = Category.objects.get(id=int(catid))
            successful_json = {'attr_name':categoryObj.category_name, 'status':categoryObj.status}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'success':False, 'message':'Server side error'}
            return HttpResponse(json.dumps(unsuccessful_json))
def fetchAttrData(request):
    if request.method == 'POST':
        try:
            attrid = int(request.POST['attrid'])
            attrObj = Attribute.objects.get(id=int(attrid))
            successful_json = {'name':attrObj.attr_name, 'status':attrObj.status}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'success':False, 'message':'Server side error'}
            return HttpResponse(json.dumps(unsuccessful_json))
def fetchStoreData(request):
    if request.method == 'POST':
        try:
            storeid = int(request.POST['store_id'])
            storeObj = Stores.objects.get(id=int(storeid))
            successful_json = {'name':storeObj.store_name, 'status':storeObj.status}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'success':False, 'message':'Server side error'}
            return HttpResponse(json.dumps(unsuccessful_json))
def editbrand(request):
    if request.method == 'POST':
        try:
            brandid = int(request.POST['brandid'])
            brandObj = Brand.objects.get(id=int(brandid))
            brandObj.brand_name = request.POST['brand_name']
            brandObj.status = request.POST['status']
            brandObj.save()
            successful_json = {'success': True, 'message': 'Success'}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'value':False}
            return HttpResponse(json.dumps(unsuccessful_json))
def editstore(request):
    if request.method == 'POST':
        try:
            storeid = int(request.POST['store_id'])
            storeObj = Stores.objects.get(id=int(storeid))
            storeObj.store_name = request.POST['store_name']
            storeObj.status = request.POST['status']
            storeObj.save()
            successful_json = {'success': True, 'message': 'Success'}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'value':False}
            return HttpResponse(json.dumps(unsuccessful_json))
def editattr(request):
    if request.method == 'POST':
        try:
            attrid = int(request.POST['attrid'])
            attrObj = Attribute.objects.get(id=int(attrid))
            attrObj.attr_name = request.POST['attr_name']
            attrObj.status = request.POST['status']
            attrObj.save()
            successful_json = {'success': True, 'message': 'Success'}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'value':False}
            return HttpResponse(json.dumps(unsuccessful_json))
def editCategory(request):
    if request.method == 'POST':
        try:
            categoryid = int(request.POST['categoryid'])
            categoryObj = Category.objects.get(id=int(categoryid))
            categoryObj.category_name = request.POST['category_name']
            categoryObj.status = request.POST['status']
            categoryObj.save()
            successful_json = {'success': True, 'message': 'Success'}
            return HttpResponse(json.dumps(successful_json))
        except Exception as e:
            print(e)
            unsuccessful_json = {'value':False}
            return HttpResponse(json.dumps(unsuccessful_json))
#view to remove group
def removegroup(request, groupid):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        grpObj = Groups.objects.get(id=int(groupid))
        grpObj.delete()
        return redirect('mainsite:managegroups')
#view to manage brands
def managecategory(request):
    if request.method == 'GET':
        allCategory = Category.objects.all()
        context = {'categories':allCategory}
        return render(request, 'managecategory.html', context)
    if request.method == 'POST':
        categoryname = request.POST['category_name']
        status = request.POST['status']
        newCatgObj = Category.objects.create(category_name=categoryname, status=status)
        newCatgObj.save()
        return redirect('mainsite:managecategory')
#view to manage brands
def managestores(request):
    if request.method == 'GET':
        allStores = Stores.objects.all()
        context = {'stores':allStores}
        return render(request, 'managestores.html', context)
    if request.method == 'POST':
        storename = request.POST['store_name']
        status = request.POST['status']
        newStoreObj = Stores.objects.create(store_name=storename, status=status)
        newStoreObj.save()
        successful_json = {'success':True, 'message': 'success'}
        return redirect('mainsite:managestores')
#view to manage brands
def manageattr(request):
    if request.method == 'GET':
        allAttributes = Attribute.objects.all()
        context = {'attributes':allAttributes}
        return render(request, 'manageattr.html', context)
    if request.method == 'POST':
        attrname = request.POST['attr_name']
        status = request.POST['status']
        newAttrObj = Attribute.objects.create(attr_name=attrname, status=status)
        newAttrObj.save()
        successful_json = {'success':True, 'message': 'success'}
        return redirect('mainsite:manageattr')
#view to add new product
def addproduct(request):
    if request.method == 'GET':
        allBrands = Brand.objects.all()
        allCategory = Category.objects.all()
        allStores = Stores.objects.all()
        print(allCategory)
        print(allStores)
        context = {'brands':allBrands, 'category':allCategory, 'stores':allStores}
        return render(request, 'addprod.html', context)
    if request.method == 'POST':
        try:
            print(request.POST)
            print(request.FILES)
            prodObj = Products.objects.create(
                picture= request.FILES['product_image'],
                sku = request.POST['sku'],
                units = request.POST['qty'],
                price = request.POST['price'],
                description = request.POST['description'],
                brand =  int(request.POST['brands']),
                category = int(request.POST['category']),
                store = int(request.POST['store']),
                availability = int(request.POST['availability'])
            )
            prodObj.save()
            return redirect('mainsite:manageproducts')
        except Exception as e:
            print(e)
            return redirect('mainsite:addproduct')
#view to manage product
def manageproducts(request):
    if request.method == 'GET':
        allProducts = Products.objects.all()
        stores = Stores.objects.all()
        context = {'products':allProducts, 'stores':stores, 'totalentries':len(allProducts)}
        return render(request, 'manageproducts.html', context)
#view to add new order
def addorder(request):
    if request.method == 'GET':
        today = datetime.today()
        allProducts = Products.objects.all()
        print(allProducts)
        context = {'products':allProducts,'date_':today.strftime('%d/%m/%y %p'), 'time_':today.strftime('%H:%M:%S')}
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
def getProductData(request):
    if request.method == 'POST':
        productName = request.POST['productName']
        prodObj = Products.objects.get(product_name=productName)
        successful_json = {'price':prodObj.price, 'qty':prodObj.units}
        return HttpResponse(json.dumps(successful_json))
#view to manage
def logout(request):
    request.session.flush()
    return redirect('users:login')

