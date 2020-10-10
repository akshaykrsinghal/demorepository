from django.contrib import admin
from django.urls import path,include
from .views.login import Login,logout
from .views.register import Register
from .views.home import home,aboutus
from .views.admin_dash import admin
from .views.student import student
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',home,name='homepage'),
    path('login/',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),
    path('logout/',logout,name='logout'),
    path('aboutus/',aboutus,name='aboutus'),
    path('admin_dash/',admin,name='admin'),
    path('student/',student,name='student'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()