#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from myshop.shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

# #Отображение формы для выбора количества товара, а второе поле проверяет если товар ранее был добавлен в корзину



@require_POST
def CartAdd(request, product_id):
     cart = Cart(request)
     product = get_object_or_404(Product, id=product_id)
     form = CartAddProductForm(request.POST)
     if form.is_valid():
         cd = form.cleaned_data
         cart.add(product=product, quantity=cd['quantity'],
                                   update_quantity=cd['update'])
     return redirect('cart:CartDetail')

# #Возможность удалять товары
def CartRemove(request, product_id):
     cart = Cart(request)
     product = get_object_or_404(Product, id=product_id)
     cart.remove(product)
     return redirect('cart:CartDetail')

# #Отображение корзины
def CartDetail(request):
     cart = Cart(request)
     return render(request, 'cart/detail.html', {'cart': cart})