from django.shortcuts import get_list_or_404
from django.views.generic import ListView
from .models import Order


class OrderListView(ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'orders/index.html'



