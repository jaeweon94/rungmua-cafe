from django.shortcuts import render, get_object_or_404
from order.models import Order, OrderItem


def index(request):
    orders = Order.objects.all()
    return render(request, 'account/index.html', {'orders':orders})
