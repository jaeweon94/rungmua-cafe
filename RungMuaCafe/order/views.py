from django.shortcuts import render

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from shop.models import Product
from django.http import HttpResponse


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

                product = Product.objects.get(name=item['product'].name)
                product.stock -= item["quantity"]
                product.save()

            cart.clear()
            request.session['order_id'] = order.id
            return HttpResponse("Ordering Complete")

    else:
        form = OrderCreateForm()

    return render(request,
                  'order/create.html',
                  {'cart': cart, 'form': form})
