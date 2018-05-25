from django.shortcuts import render, reverse
from shop.models import ItemsInCart
from .models import Order
from decimal import Decimal
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

def index(request):
	session_key = request.session.session_key
	items = ItemsInCart.objects.filter(session_key=session_key, is_active=True)
	order = Order.objects.create(session_key=session_key)
	order.save()
	order.ordered_items.add(*items)
	order.save()

	total_order_price = 0
	for item in items:
		total_order_price += item.total_price
	request.session['total_cost'] = total_order_price

	context = {
		'items': items,
		'total_price': total_order_price,
	}


	return render(request, 'checkout.html', context)


def PaymentProcess(request):
	data = request.POST
	name = data.get('name')
	phone = data.get('phone')
	email = data.get('email')
	city = data.get('city')
	street_address = data.get('address_1')
	house_address = data.get('address_2')
	details = data.get('order_comments')
	cost = Decimal(request.session.get('total_cost'))
	order = Order.objects.create(name=name, phone=phone, email=email, delivery_address=' '.join((city, street_address, house_address)), details=details, cost=cost)
	print(order.cost, type(order.cost))
	host = request.get_host()

	paypal_dict = {
		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'amount': '%.2f' % order.cost.quantize(Decimal('.01')),
		'item_name': 'Заказ {}'.format(order.id),
		'invoice': str(order.id),
		'currency_code': 'RUB',
		'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
		'return_url': 'http://{}{}'.format(host, reverse('checkout:done')),
		'cancel_return': 'http://{}{}'.format(host, reverse('checkout:canceled'))
	}

	form = PayPalPaymentsForm(initial=paypal_dict)
	return render(request, 'process.html',{'order':order, 'form':form})




@csrf_exempt
def PaymentDone(request):
    return render(request, 'done.html')

@csrf_exempt
def PaymentCanceled(request):
    return render(request, 'canceled.html')