from django.shortcuts import render

# Create your views here.


def checkout(request):
    """
    The view that handles checkouts
    """

    return render(request, 'checkout/checkout.html')