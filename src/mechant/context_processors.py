from lzma import MODE_FAST
from front import models


def get_total_number_products(request) -> dict:
    total_products = 0
    session_id = request.session._get_or_create_session_key()
    orders = models.OrderItem.objects.filter(session_id=session_id)
    
    for order in orders: total_products += order.quantity
    
    return {"total_products": total_products}

def get_product_cart_count(request):
    session_id = request.session._get_or_create_session_key()
    
    catrs_count = models.Cart.objects.filter(session_id = session_id).count
    return {"carts_count":catrs_count}