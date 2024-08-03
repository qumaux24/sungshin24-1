from django.urls import path
from . import views
from accounts.urls import login, signup

urlpatterns = [
    path('', views.list, name='list'),
    path('signup/', signup, name='signup'),
    path('login', login, name='login')
]
