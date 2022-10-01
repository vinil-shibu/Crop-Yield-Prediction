from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('reg',views.reg,name='reg'),
    path('yield',views.p_yield,name='yield'),
    path('logout',views.logout,name='logout')
]