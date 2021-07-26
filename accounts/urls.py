from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accounts.views import hello_world, AccountsCreateView

app_name = "accounts"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountsCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
