from front import models


def get_total_number_products(request) -> dict:
    """Cette fonction va permetre de calculer le nombre
    total de produit dans le panier de l'utilisateur quand
    il est connecté"""
    
    total_quantity_product = 0
    
    try:    
        orders = models.Cart.objects.get(user=request.user).order.all()
        for order in orders: total_quantity_product += order.quantity
    except models.Cart.DoesNotExist:
        pass
    except TypeError:
        pass

    return {"total_products": total_quantity_product}


def get_total_number_products_user_anonyme(request) -> dict:
    total_products = [item["quantity"] for item in request.session.get("cart", [])]
    return {"total_products": sum(total_products)}
    
    
    
    