# from django.shortcuts import render (uncomment to use later)
from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """
    A view to display all products in a list,
    sorting,
    search queries
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
