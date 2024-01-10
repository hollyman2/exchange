from django.urls import path
from . import views


urlpatterns = [
    path('add_order/', views.AddOrderView.as_view(), name='add_order'),
]
