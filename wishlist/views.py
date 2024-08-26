from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Wishlist
from destinations.models import Destination


@login_required
def add_to_wishlist(request, destination_id):
    destination_wishlist = get_object_or_404(Destination, id=destination_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if destination_wishlist not in wishlist.destinations.all():
        wishlist.destinations.add(destination_wishlist)
        messages.success(request, f'{destination_wishlist.name} foi adicionado à sua lista de desejos.')
    else:
        messages.info(request, f'{destination_wishlist.name} já está na sua lista de desejos.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist_view.html', {'wishlist': wishlist})


@login_required
def remove_from_wishlist(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)

    if destination in wishlist.destinations.all():
        wishlist.destinations.remove(destination)
        messages.success(request, f'{destination.name} foi removido da sua lista de desejos.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
