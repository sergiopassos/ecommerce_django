from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed


from products.models import Product
User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
	def new_or_get(self, request):
		cart_id = request.session.get("cart_id", None)
		qs = self.get_queryset().filter(id=cart_id)
		if qs.count() == 1:
			new_obj = False
			cart_obj = qs.first()
			if request.user.is_authenticated() and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()
		else:
			cart_obj = Cart.objects.new(user=request.user)
			new_obj = True
			request.session['cart_id'] = cart_obj.id
		return cart_obj, new_obj


	def new(self, user=None):
		print(user)
		user_obj = None
		if user is not None:
			if user.is_authenticated():
				user_obj = user_obj
		return self.model.objects.create(user=user_obj)

class Cart(models.Model):
	user 		= models.ForeignKey(User, null=True, blank=True)
	products 	= models.ManyToManyField(Product, blank=True)
	subtotal	= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	total		= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	update		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	objects = CartManager()

	def __str__(self):
		return str(self.id)

def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
	if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
		print(action)
		products = instance.products.all()
		total = 0
		for x in products:
			total += x.price
		instance.subtotal = total
		instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)

def pre_save_cart_receiver(sender, instance, *arg, **kwargs):
	if instance.subtotal > 0:
		instance.total = Decimal(instance.subtotal) * Decimal(1.08) #  8% tax
	else:
		instance.total = Decimal(0.00)

pre_save.connect(pre_save_cart_receiver, sender=Cart)