from django.contrib import admin
from django.urls import path
from regapp import views
urlpatterns = [
 path('',views.signUp,name='home'),
 path('signup',views.signUp,name='signup'),
 path('log_in',views.log_in,name='log_in'),
 path('index',views.index, name="index")
]