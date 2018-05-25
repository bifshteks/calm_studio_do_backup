from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'
    verbose_name = 'Оплата'

    def ready(self):
        import checkout.signals
