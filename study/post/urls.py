from django.urls import path
from . import views
from accounts.views import login, signup, logout, return_main

urlpatterns = [
    path('', views.list, name='list'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', return_main, name='return_main')
]
