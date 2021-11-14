# from django.shortcuts import render (uncomment to use later)
from django.views.generic import ListView

# Create your views here.


class Memberships(ListView):
    """
    The view that lists all memberships including search queries
    """
    template_name = 'membership/memberships.html'
