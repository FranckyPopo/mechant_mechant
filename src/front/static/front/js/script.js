span_checkout_items = document.querySelector("#checkout_items")

function toast(text, e) {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000
      })
      
      Toast.fire({
        icon: 'success',
        title: text
      })
    span_checkout_items.innerHTML = e.detail.total_products
}

htmx.on("product_add_cart", function (e){
    toast("Produit ajouter au panier", e)
});

htmx.on("product_delete_cart", function (e){
    toast("Produit supprimer du panier", e)
});
