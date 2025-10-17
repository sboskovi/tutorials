# Templating engines

## Pug
https://pugjs.org/api/getting-started.html
Indentacija je bitna

Treba naznaciti expressu da koristi templating engine
```
app.set("view engine", "pug")
app.set("views", "my-views-folder")
```

### Renderovanje i prosljedjivanje podataka template-u
Za slanje fajlova klijentu koristi se funkcija render, 
```
res.render('my-page-in-views-folder', { prods: products })
```

### if and for
Mogu se koristiti if-ovi u template-u:
```
.pug
if prods.length > 0
	each product in prods
		h1 #{product.title}
else
	h1 No Products
```

Mogu i for petlje:
```
each product in prods
	h1.my-class #{product.title}
```

### Layout and hooks
Moguce je napraviti **layout** za vise stranica i **hook**-ove sa kljucnom rijecju **block** koji se definisu u pojedinacnim stranicama
```
block styles
...
block content
```

U pojedinacnim stranicima to bi izgledalo ovako:
```
extends layouts/main-layout.pug

block content
	main
		h1.error-style Page Not Found na primjer
```