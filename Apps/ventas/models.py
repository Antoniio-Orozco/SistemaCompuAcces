import uuid
from django.db import models
from Apps.administracion.models import Producto
from Apps.cliente.models import Cliente
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed, pre_save, post_save
# Create your models here.


class Venta(models.Model):
    empleado = models.ForeignKey(User, null=True, blank=True ,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True, blank=True ,on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(default=0.0,max_digits=8, decimal_places=2)


class Cart(models.Model):
    cart_id = models.CharField(max_length= 100, null= False, blank = False, unique = True)
    empleado = models.ForeignKey(User, null=True, blank=True ,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True, blank=True ,on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto, through='CartProducts')
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(default=0.0,max_digits=8, decimal_places=2)


    def __str__(self):
        return '%s %s' % (self.fecha,self.empleado)

    def update_totals (self):
        self.total = sum([ 
          cp.quantity * cp.product.precio   for cp in self.products_related()
        ])
        self.save()    

    def products_related(self):
        return self.cartproducts_set.select_related('product')

def set_cart_id(sender, instance, *arg, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())       

class CartProductsManager(models.Manager):

    def createOrUpdateQuantity(self, cart, product, quantity=1):
        object, created =   self.get_or_create(cart=cart, product=product)

        if not created:
            quantity = object.quantity +  quantity

        object.updateQuantity(quantity)

        return object

class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    fecha = models.DateField(auto_now_add=True)

    objects = CartProductsManager()

    def updateQuantity(self, quantity=1):
        self.quantity = quantity
        self.save()

def updateTotals (sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()

def postSaveUpdateTotals(sender, instance, *args, **kwargs):
    instance.cart.update_totals()


pre_save.connect(set_cart_id, sender = Cart)
post_save.connect(postSaveUpdateTotals, sender = CartProducts)
m2m_changed.connect(updateTotals, sender = Cart.producto.through)