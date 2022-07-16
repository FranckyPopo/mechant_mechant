span_checkout_items = document.querySelector("#checkout_items")

htmx.on("order_add", function (e){
    
    span_checkout_items.innerHTML = e.detail.total_products
});
