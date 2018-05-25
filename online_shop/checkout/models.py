# -*- coding: utf-8 -*-
from django.db import models
from shop.models import ItemsInCart

class Order(models.Model):

    OPEN = 'Открыт'
    PROCESS = 'В процессе'
    PAID = 'Оплачен'
    DELIVERIED = 'Доставлен'
    CLOSED = 'Закрыт'
    CHOICES = (
        (OPEN, 'Открыт'),
	    (PROCESS, 'В процессе'),
	    (PAID, 'Оплачен'),
	    (DELIVERIED, 'Доставлен'),
	    (CLOSED, 'Закрыт'),
    )

    session_key =  models.CharField(max_length=255, verbose_name="Сессия", blank=True, null=True, default=None)
    name = models.CharField(verbose_name="Имя", max_length=255, blank=True, null=True, default=None)
    email = models.CharField(verbose_name="E-mail", max_length=255, blank=True, null=True, default=None)
    phone = models.CharField(verbose_name="Телефон", max_length=20, blank=True, null=True, default=None)
    ordered_items = models.ManyToManyField(ItemsInCart, blank=True, null=True, default=None)
    delivery_address = models.TextField(verbose_name="Адрес доставки", blank=True, null=True, default=None)
    details = models.TextField(verbose_name="Детали к заказу", blank=True, null=True, default=None)
    cost = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Полная стоимость заказа", blank=True, null=True, default=None)
    status = models.CharField(verbose_name="Статус", max_length=2, choices=CHOICES, default=OPEN)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        if self.name:
            return self.name + ' ' + self.phone
        elif self.session_key:
            return self.session_key
        else:
            return 'Empty object'

