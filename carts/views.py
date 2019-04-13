from django.shortcuts import render
from django.views import View

from .models import Cart

# def cart_home(request):
# 	cart_obj = Cart.objects.new_or_get(request)
# 	return render(request, "carts/home.html", {})

class HomeCartView(View):
	def get(self, request):
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		total = 0
		products = cart_obj.products.all()
		for produto in products:
			total += produto.price
		print(total)
		cart_obj.total = total
		cart_obj.save()
		return render(request, "carts/home.html", {})