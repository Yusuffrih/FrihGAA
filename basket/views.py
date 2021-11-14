from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """
    The view that returns the basket template
    """

    return render(request, 'basket/view_basket.html')
