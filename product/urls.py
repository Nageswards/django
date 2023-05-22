

from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.login, name='home'),
    path('category', views.category, name='home')
]