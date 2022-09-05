from django.urls import path
from .views import Home, additems, delete, checkout, confirm, logout, adduser, manageuser, \
    addgroups, managegroups, managebrands, managecategory, managestores, manageattr, addproduct, \
    manageproducts, addorder, manageorder, reports, company, profile, settings, removegroup,removebrand, editbrand, fetchBrandData, \
    fetchCategoryData, editCategory, removeCategory, fetchStoreData, editstore, removestore, fetchAttrData, editattr, removeAttr, \
    removeproduct, getProductData


app_name='mainsite'

urlpatterns = [
    path('', Home, name='Home'),
    path('additems', additems, name='additems'),
    path('checkout', checkout, name='checkout'),
    path('adduser', adduser, name='adduser'),
    path('manageuser', manageuser, name='manageuser'),
    path('addproduct', addproduct, name='addproduct'),
    path('managebrands', managebrands, name='managebrands'),
    path('managecategory', managecategory, name='managecategory'),
    path('managegroups', managegroups, name='managegroups'),
    path('manageproducts', manageproducts, name='manageproducts'),
    path('managestores', managestores, name='managestores'),
    path('manageattr', manageattr, name='manageattr'),
    path('addgroups', addgroups, name='addgroups'),
    path('removegroup/<int:groupid>', removegroup, name='removegroup'),
    path('removebrand', removebrand, name='removebrand'),
    path('getProductData', getProductData, name='getProductData'),
    path('removeproduct', removeproduct, name='removeproduct'),
    path('removeAttr', removeAttr, name='removeAttr'),
    path('removestore', removestore, name='removestore'),
    path('removeCategory', removeCategory, name='removeCategory'),
    path('editbrand', editbrand, name='editbrand'),
    path('editstore', editstore, name='editstore'),
    path('editCategory', editCategory, name='editCategory'),
    path('editattr', editattr, name='editattr'),
    path('fetchBrandData', fetchBrandData, name='fetchBrandData'),
    path('fetchStoreData', fetchStoreData, name='fetchStoreData'),
    path('fetchCategoryData', fetchCategoryData, name='fetchCategoryData'),
    path('fetchAttrData', fetchAttrData, name='fetchAttrData'),
    path('addorder', addorder, name='addorder'),
    path('manageorder', manageorder, name='manageorder'),
    path('settings', settings, name='settings'),
    path('company', company, name='company'),
    path('profile', profile, name='profile'),
    path('reports', reports, name='reports'),
    path('logout', logout, name='logout'),
    path('confirm', confirm, name='confirm'),
    path('delete/<int:prodid>', delete, name='delete'),

]