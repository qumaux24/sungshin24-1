from django.urls import path
from .views.login_views import signup, login, logout, findPW
from .views.passkey_views import Passkey
from .views.userdetail_views import user_detail


app_name="accounts"

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('user_detail/', user_detail, name='user_detail'),
    path('findPW/', findPW, name='findPW'),
    path('passkey', Passkey, name='passkey'),
]
