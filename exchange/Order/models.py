from django.db import models
import uuid
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class Order(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    author = models.CharField(max_length=100)
    contractual = models.BooleanField(default=True)
    price = models.DecimalField(
        blank=True, null=True, max_length=7, decimal_places=3, max_digits=7)
    # date_added = models.DateTimeField(default=timezone.now())
    tags = TaggableManager()

    def __str__(self):
        return self.title[0:25]

    def get_absolute_url(self):
        return reverse("/", kwargs={"id": self.id})
    
    # class Meta:
    #     ordering = ['date_added']
