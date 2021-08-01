from django.urls import path

from subscribeapp.views import SubscriptionView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe')
]  # FIXME: <int:pk> 없었는데 넣으면?
