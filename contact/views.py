from django.shortcuts import render
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm

# Create your views here.


def contact(request):
    """ Access contact page and submit form """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your enquiry. \
                             We will get back to you as soon as possible!")

            instance = form.save()
            # Send email confirming message received
            sender_email = instance.email
            subject = render_to_string(
                'contact/confirmation_emails/acknowledgement_subject.txt',
                {'instance': instance})
            content = render_to_string(
                'contact/confirmation_emails/acknowledgement_content.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                content,
                settings.DEFAULT_FROM_EMAIL,
                [sender_email],
            )
            context = {
                'form': form
            }

            return render(request, 'contact/contact_success.html', context)

        else:
            messages.error(request, 'Message not sent.'
                           ' Please ensure the form is valid!')
    else:
        template = 'contact/contact.html'
        form = ContactForm()
        context = {
            'form': form,
        }

        return render(request, template, context)
