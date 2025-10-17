# Analiza razgovora za scribe
<b>NOTE</b> oznacava mjesta gdje sam grijesio

# Pregled gresaka:
1. Dohvatanje user model-a. Umjesto da si guglao odmah `djagno get user model` ti si lutao po dokumentaciji kako da dohvatis user model.
2. Problem sa serializer-ima. Nisi znao kako da uradis FK u njima a opet si pisao njih. DOk ti na kraju nije rekao da napravis bez njih.
3. Izgubio si se trazeci FK u serijalizerima a nisi znao konceptualno sta je to niti si ikad korisito.
4. Mislio si da postoji funkcija koja pretvara model u dictionary. I jos manje da ukljucis FK-ove
5. Nisi znao kako da definises FK na sam model


# Konceptualne greske
1. Dohvatanje user modela
2. Nedovoljno poznavnje serialzier-a
3. Nedovoljno poznavanje FK-a
4. Pretvaranje Model objekata u dict
5. Lutanje po dokumentaciji umjesto guglanje i otvaranje stack overflow-a