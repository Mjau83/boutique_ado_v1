from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J8kgXH04Mk3IwYLrLOBKDoUBPSPyg897dVc5qTiLCCYyMZQrwWjLcuNB2juzwwsj2LAsHCpyEZ5z7hXhJTZySgH00Z4LIqPRM',
        'client_secret':'test client sec',
    }

    return render(request, template, context)