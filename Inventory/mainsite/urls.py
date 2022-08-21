from django.urls import path
from .views import Home, additems, delete

app_name='mainsite'

urlpatterns = [
    path('', Home, name='Home'),
    path('additems', additems, name='additems'),
    path('delete/<int:prodid>', delete, name='delete'),

]