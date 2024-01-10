from django.shortcuts import get_list_or_404
from django.views.generic import ListView, View, CreateView
from .models import Order


class OrderListView(ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'orders/index.html'

class SearchOrderView(ListView):

    template_name = 'orders/index.html'
    context_object_name = 'order_list'

    def get_queryset(self):
        return Order.objects.filter(tags=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

class AddOrderView(CreateView):
    model = Order
    fields = ['']

