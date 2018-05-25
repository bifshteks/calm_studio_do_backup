from django.conf.urls import url
import checkout.views as cv

urlpatterns = [
	#url(r'', , name=""),
	url(r'^$', cv.index , name="checkout"),	
	url(r'^process/$', cv.PaymentProcess, name="process"),
	url(r'^done/$', cv.PaymentDone, name="done"),
	url(r'^canceled/$', cv.PaymentCanceled, name="canceled"),

]