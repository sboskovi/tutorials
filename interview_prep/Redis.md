# Redis
Single threaded, in memory, data structure server. Cuva podatke u memoriji ali ih i perzistra na disk u odredenjim intervalima, default je npr 1 min. Hash mapa u sustni.
- Izvrsava se obicno na vise node-ova (servera)
- Svaki node obicno ima **secondary** koji drzi kopiju podataka i moze ulogu **main** node-a ukoliko ovaj padne
- Node padne -> secondary preuzima. Podaci se cuvaju i u bazi da mogu da se rekonstruisu
- Cluster - vise main / secundary node-ova
- Key odredjuje kako se shard-uje redis - kako su podaci rasporedjeni izmedju node-ova
- Hot key - append values to keys da se rasporedi na vise node-ova?
- Expiration policy - LRU npr

## Osnovne funkcije
- SET
- GET
- INCR # increment value
- EXPIRE key 60 LT # vrijednost ovog key-a se setuje na 0 nakon 60s
- GEOADD - dodaje 
- GEOSEARCH key FROMLONLAT longitude latitude BYRADIUS 5km WITHDIST

## Use case-ovi
- Cache 
- Rate Limiter
- Streams - slicno kafki - imas stream, consumer group i worker-e
- Geoindexi i geolokacija
- Pub Sub