from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def contact(request):
    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
