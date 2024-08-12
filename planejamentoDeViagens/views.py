from django.shortcuts import render

from destinations.models import Destination


def home(request):
    return render(request, 'home.html')



