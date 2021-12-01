# from django.shortcuts import render (uncomment to use later)
from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    A view to display specific product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
