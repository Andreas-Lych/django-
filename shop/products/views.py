import logging
from django.http import HttpResponse

from products.models import Product

from products.forms import AddProduct
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    products = Product.objects.all()

    title = request.GET.get("title")
    if title is not None:
        products = products.filter(title__icontains=title)

    purchases__count = request.GET.get("purchases__count")
    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    return render(request, "index.html", {"products": products}  )

def addproduct(request):
        form = AddProduct()
        return render(request, "addproduct.html", {"form": form})