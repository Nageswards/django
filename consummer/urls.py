from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
    path("user/<int:id>",User_get,name="User_get"),
    path("user_based",user_based,name="user_based"),
    path("login",login,name="login"),
    path("image",Home.as_view(),name="image")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
