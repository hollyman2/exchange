from django.urls import reverse_lazy
from Order.models import Order
from django.views.generic import ListView, View, CreateView


'''class Order(models.Model):
    # id = models.UUIDField( 
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    contractual = models.BooleanField(default=True)
    price = models.DecimalField(
        blank=True, null=True, max_length=7, decimal_places=3, max_digits=7)
    date_added = models.DateTimeField(timezone.now())
    tags = TaggableManager()'''

class AddOrderView(CreateView):
    model = Order
    fields = ['title','description','price','tags']
    success_url = reverse_lazy('order_detail')
    template_name = 'client/add_order.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super(AddOrderView,self).form_valid(form)
    
