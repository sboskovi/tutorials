# Lotus pitanja

## Kako dizajnirati Task Scheduler

## Hash Maps, implementacija i rjesavanje kolizija?

## Prednosti i mane mikroservisne arhitekture

## Da li moze monolit da se skalira?
- Moze do odredjene mjere - samo nije skalabilan. 
- Granice vertikalnog skaliranja
- Otezava rad na programu


## Zasto ne dodati index na svaku kolonu:
1. Usporava upis u bazu - INSERT, UPDATE, DELETE jer za svaku od tih op. moraju da se azuriraju indexi
2. Zauzimaju dodatni prostor i dodatnu memoriju
3. Query planner ne zna koji index da prioritizuje za optimiziaciju
NOTE: Query planner parsira SQL upit i odredjuje koje indexe da koristi, zajedno sa drugim optimizacijama koje obavlja.

##


## Sta se desi kada ukucas google.com u browser-u?
1. **Browser URL parse** - ako je validan nastavi sa stavkom 2, ako nije npr pokreni google pretragu za taj URL.
2. **Cached Page** - Trazi da li stranica postoji u **browser cache**-u i ako nije stale - preko **header**-a npr `Cache-Control`. Ili browser koristi neku heuristiku da odredi da li je fresh.
3. **DNS Lookup** - cache OS-a ili DNS lookup
4. **TCP** ili **QUIC** konekcija - **TCP 3 way handshake** ili savremenije - **QUIC / HTTP3** (Preko UDP-a). (Transportni sloj)
5. **TLS / Certificate** verifikacija. U prehodnom koraku klijent dobija sertifikat, tako da moze da provjeri kod CA (certification authority) da je to validan server.
6. **HTTP Request** - salje se sam zahtjev da se dohvati stranica na datu IP adresu
7. **Networking and CDN** - zahtjev stize do CDN-a ili load balansera data centra. Ako je ahtjev kesiran, vraca se iz kesa, ako nije prosljedjuje se web serverima.
8. **Server side Handling** - Web server obradjuje zahtjev i vraca response.
9. **Response travels back**
10. **Browser renders response** - browser parsira **HTML** i konstruise **DOM**, dohvata **CSS, JS, Images**. JS izvrsava dodatne zahtjeve za generisanje dinamickog sadrzaja.
11. **Post-load** - browser cuva **cookies** - po URL-u (domain). Browser moze da otvori **WebSocket** stream npr.

### Sta je SSL?
- Transport layer? (OSI 4?)
- Secure socket layer - kriptografski protokol za sigurnu internet komunikaciju.
- Zastario, zamijenio ga se **TSL** - Transport Layer Security

### Sta je CA?
- Certificate authority, izdaje sertifikate i potvrdjuje njihovu ispravnost.

## Kako se balnsiraju zathjevi ka google-u?


## Sta su DB indexi? Zasto ne staviti index na svaku kolonu? Index na string? Index na bool?
- B stabla? Za lakse pretrazivanje podataka po toj koloni.
- Ne stavlja se na svakoj kolini jer zauzimaju dodatni prostor, i usporavaju operacije nad podacima?

## Replicate u Postgres-u, Master / Slave replikacija

## Load balansing i sesije, kako load balanser zna koju masinu da gadja?
- Sticky session ili consistent hasing?
- Consistent hasing bolji jer je skalabiliniji. Lakse je u takvom sistemu dodavati i uklanjati masine.

## Da li uvijek gadjas isti DNS
- Obicno GeoLocirani zbog brzeg pristupa
- Moguce je rucno podesiti na svom racunaru
- Ako pristupas sa kucne mreze, gadjas DNS ISP-a (Internet Service Provider) koji ISP moze da promijeni
- Ako pristupas sa VPN-a gadjas DNS koji ti odredi VPN provider