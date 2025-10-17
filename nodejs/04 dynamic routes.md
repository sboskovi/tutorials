# Query params
```
router.get("proudcts/:productId", () => {
	const productId = req.params.productId;
})
```

Postavljanjem hidden input polja u formu mozemo da ga submitt-ujemo kao dodatu vrijednost POST request-a:
```
<form action="/cart" method="post">
	<button type="submit">Add to cart</button>
	<input type="hidden" name="productId" value="<%= product.id %>">
</form>
```