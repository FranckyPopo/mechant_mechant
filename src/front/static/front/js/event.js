htmx.on("Bon", function(evt) {
    console.log(evt.detail.value[0])
    document.cookie = null
});