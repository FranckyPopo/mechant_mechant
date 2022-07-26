from front import models


def get_total_number_products(request) -> dict:
    """Cette fonction va permetre de calculer le nombre
    total de produit dans le panier de l'utilisateur quand
    il est connecté ou non"""
    
    if request.user.is_authenticated:
        total_quantity_product = 0
        cart, _ = models.Cart.objects.get_or_create(user=request.user, ordered=False)
        for order in cart.order.all(): total_quantity_product += order.quantity
        
        return {"total_products": total_quantity_product}
    else:
        total_products = [item["quantity"] for item in request.session.get("cart", [])]
        return {"total_products": sum(total_products)}
        