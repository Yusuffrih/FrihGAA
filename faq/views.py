from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Faq
from .forms import FaqForm

# Create your views here.


def faq(request):
    """ Display the FAQs """
    faq = Faq.objects.all()

    template = 'faq/faq.html'
    context = {
        'faq': faq,
    }

    return render(request, template, context)


def add_faq(request):
    """ Add an faq to the database and faq page """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Frih GAA admin can do this.')
        return redirect(reverse('faq'))

    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ successfully added!')
            return redirect(reverse('faq'))
        else:
            messages.error(
                request,
                "Couldn't add the FAQ.\
                    Please check the form is valid and try again")
    else:
        form = FaqForm()

    template = 'faq/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
