import logging
from django.http import HttpResponse

from products.models import Product

logger = logging.getLogger(__name__)


def index(request):
    products = Product.objects.all()
    query = request.GET.get("query")
    if query is not None:
        products = products.filter(title__icontains=query)
    string = "<br>".join([str(p) for p in products])
    return HttpResponse(string)

from django.shortcuts import render

# Create your views here.
