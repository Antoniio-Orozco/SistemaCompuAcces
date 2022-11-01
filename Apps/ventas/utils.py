from .models import Cart

def getOrCreateCart(request):
    user = request.user if request.user.is_authenticated else  None
    
    #Intentamos buscar el carrito
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(cart_id=cart_id).first()
    
    #Si el carrito no existe, lo crea
    if cart is None:
        cart = Cart.objects.create(empleado= user)
    
    if user and cart.empleado is None:
        cart.empleado = user
        cart.save()
    

    request.session['cart_id'] = cart.cart_id #actualizar la sesion
    
    return cart

def destroyCart(request):
    request.session['cart_id'] = None