from django.urls import path

from subscribeapp.views import SubscriptionView, SubscriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    path('list/', SubscriptionListView.as_view(), name='list'),
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
]
