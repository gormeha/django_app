from django.urls import path
from myapp import views
from  myapp.views import *
from django.contrib.auth import views as auth_views
app_name = 'myapp'
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 path(r'login/', views.user_login, name='login'),
 path(r'logout/', views.user_logout, name='logout'),
 path(r'', IndexView.as_view(), name='index'),
 path(r'about/', views.about, name='about'),
 path(r'detail/<int:cat_no>', views.detail, name='details'),
 path(r'products/',views.products,name='products'),
 path(r'place_order/', views.place_order,name='place_order'),
 path(r'products/<prod_id>', views.productdetail, name='productdetail'),
 path(r'order/', views.myorders, name='my_order'),
 path(r'register/', views.register, name='register')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)