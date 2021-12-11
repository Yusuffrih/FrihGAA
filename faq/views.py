from django.shortcuts import render
from .models import Faq

# Create your views here.


def faq(request):
    """ Display the FAQs """
    faq = Faq.objects.all()

    template = 'faq/faq.html'
    context = {
        'faq': faq,
    }

    return render(request, template, context)
