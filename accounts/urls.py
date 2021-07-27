from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accounts.views import hello_world, AccountsCreateView, AccountsDetailView, AccountsUpdateView, AccountsDeleteView

app_name = "accounts"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    # login, logout
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # create, detail, update, delete
    path('create/', AccountsCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountsDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountsDeleteView.as_view(), name='delete'),
]
