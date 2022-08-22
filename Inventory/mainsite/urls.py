from django.urls import path
from .views import Home, additems, delete, checkout, confirm, logout

app_name='mainsite'

urlpatterns = [
    path('', Home, name='Home'),
    path('additems', additems, name='additems'),
    path('checkout', checkout, name='checkout'),
    path('logout', logout, name='logout'),
    path('confirm', confirm, name='confirm'),
    path('delete/<int:prodid>', delete, name='delete'),

]