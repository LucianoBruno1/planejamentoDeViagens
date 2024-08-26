from django.shortcuts import render
from .models import Destination


def destination_list(request):
    continent = request.GET.get('continent')

    if continent:
        destinations = Destination.objects.filter(continent=continent)
    else:
        destinations = Destination.objects.all()

    return render(request, 'destination_list.html', {'destinations': destinations})
