from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrderListView.as_view(), name='order_list'),
    path('search/', views.SearchOrderView.as_view(), name='search'),
]
