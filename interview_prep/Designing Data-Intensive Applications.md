# Designing data intensive applications

# Vrati se na prethonda poglavlja i podsjeti se:
- Rolling release
- Format fajla za cuvanje podataka u bazi

### Data Models and Query Langugages
- Document modeli su dobri kada nemas veze (relationships) izmedju podataka
- Relacije postoje i u Document modelima
- Relacioni model dobar kada imas veze, nije dobar kada imas mnogo many to many veza
- Za mnogo many to many veza pogodniji **Graph-Like Data** modeli

Facebook je modelirao podatke kao heterogeni graf - ljudi, lokacije i komentari su cvorovi (vertices, nodes) dok veze (edges) 
oznacavaju koji ljudi su prijatelji, ko je komentarisao na koju sliku, itd.


# ---------- Chapter 5 - Replication ----------
Replikacija podataka - odrzavanje kopije podataka na vise masina iz sledecih razloga:
- **Latency** - Da bi podaci bili geogrfski blizu korisnicima da bi se smanjio latency.
- **Availability** - u slucaju otkaza pojedinacne masine da sistem nastavi da radi.
- **Scalability** - da se poveca broj masina koje mogu da citaju podatke.

**Pretpostavka**: svi podaci mogu da stanu na jednu masinu (bazu podataka). 
**Partitioning** ili **sharding** ako podaci ne mogu da stanu na jednu masinu. 

### Replication algorithms
- Single leader
- Multi leader
- Leaderless


### Leaders and followers
Prilikom upisa u bazu moramo da azuriramo baze u svim replikama:
1. Jedna replika se oznaci kao *leader*. Prilikom upisa, zahtjev mora ici leader-u koji upisuje podatke u svoju bazu.
2. Ostale replike se oznace kao *followers*. Kada leader upise podatke u svoju bazu on salje te podatke follower-ima u obliku **replication log**-a ili **change stream**-a. 
Svaki follower upisuje podatke u svoju bazu na onaj nacin kako je opisano u log-u.
3. Klijent cita podatke kod leader-a ili follower-a, ali write radi samo u leader-a.

Ovo je ugradjen nacin replikacije podataka u mnoge relacione i u neke nerelacione baze podataka. Kafka isto koristi.

### Handling node outages
Follower-e je lako zamijeniti kad neki od njih fail-uje. Za leadere je malo slozenije:
1. Ustanoviti da je leader fail-ovao. Rucno ili u slucaju da je leader non responsive neko vrijeme (30s npr).
2. Izabrati novog leader-a.
3. Rekonfigurisati sistem da koristi novog leader-a. 

Koji su problemi:
- Novi leader mozda nema sve podatke koji su upisani u starog leader-a. Moguci pristup je odbaciti podatke koje ima stari leader.
- Moguce je da dva Node-a misle da su leader.

### Implementation of Replicaiton logs
- Statement log - salje se svaki insert, update i delete follower-ima koji onda izvrsvanju iste komande. Problem su nedeterministicke funkcije tipa - RAND(), NOW(), ...
- Write ahead log (WAL) shiping. Ako baza cuva podatke kao **SSTables** i **LSM-Trees** ili **B-trees** log je append-only sekvenca bajtova koja sadrzi sve upise u bazu. Koriste PostreSQL i Oracle. Ovdje su nacin cuvanja podataka na disku i log direktno povezani.
- Logical (row based) log - log struktura je razdvojena (razlicita) od nacina cuvanja podataka na disku.
- Trigger based replication - Trigger na data change operaciju da cuva sve izmjene u zasebnoj tabeli odakle moze da se cita od strane nezavisnog procesa. Ovim se premjesta failover logika u aplikativni sloj.

## Problems with replication lag-om
Problem sa distribuiranim bazama kako imati konzistentne podatke medju leader-ima i follower-ima. Sledeci problemi i koncepti postoje:
### Reading your own writes
Korisnik nakon sto upise neki podatak kod leader-a ocekuje isti podatak odmah i da procita od follower-a. U suprotnom stice utisak da podaci nisu sacuvani.
**Read after write consistency**:
- Ako je korisnik modifikovao neke podatke, podaci koji su *mozda* modifikovani se citaju iz leader-a. Korisno za korisnicka podesvanja, nije skalabilno.
- Pracenje zadnjeg trenutka upisa od strane korisnika. Citanja koja se dese od tog trenutka +1min npr idu od leader-a, nakon toga od follow-ra.
- Na osnovu trenutka upisa i ocekivanog replication lag-a, moze da se odredi koji follower je spreman za read.
**Cross device read-after-write**: Ako kosinik pristupa podacima sa razlicitih uredjaja. Npr sa racunara i sa telefona koji je na mobilnoj mrezi. To su dvije potpuno razlicite mreze i mozda read zahtjevi odu na potpuno razlicite follower-e ili cak data centre.
### Monotonic reads
Situacija: u prvom citanju korisnik cita podatak od 1. followera koji ima azurne podatke, u drugom citanju cita podatak od 2. follower-a koji jos nema taj podatak i korisnik stice utisak da je podatak obrisan. **Monotonic reads** garantuje da se ovo ne desi - npr. mapiranjem korisnika po hash-u ID-a na follower-a.
### Consistent prefix reads
Situacija u kojoj korisnik prvo cita odgovor pa tek onda pitanje (u komentarima npr). Problematicno kod particionisanih podataka (sharded database). Rjesenje je upisivati podatke koji su povezani u istu particiju.


## Multi leader replication
Glavna primjena je u sistemima gdje se koristi vise data centara za skladistenje podataka. Primjena u jednom data centru obicno dodaje vise kompleksnosti nego koristi.
Problem su konflikti prilikom upisa u razlicitim data centrima. Za to treba da se primjeni neki **conflict resolution**. **Autoincrment keys**, **triggers** i **integrity constraints** mogu da budu problem u ovakvim sistemima. Zbog ovoga se cesto smatra opasnom i treba je izbjegavati ako je moguce.

### Clients with offline operations 
Primjer je *kalendar* na telefonu. Cak i ako nemas pristup internetu mozes da zakazujes sastanke a nakon dobijanja pristupa internetu treba sinhronizovati sa svim ostalim kalendarima (npr svih ljudi koji su pozvani na sastanke). U ovom slucaju svaki telefon ima svoju bazu i baze podataka izmedju svih njih koje ih povezuju.
### Colaborative editing
Google docs npr moze da edituje vise korisnika od jednom. Moguce je zakljucati dokument kad ga edituje jedan korisnik, ali bolje je rjesenje sinhronizovati klijente na recimo *keystroke*. Tako korisnici dobijaju interaktivnije iskustvo i ne mora da se zakljucava dokumnet za write.
### Handling write conflicts
Situacija: prvi korisnik  promijeni naslov dokumenta iz **A** u **B** a drugi iz **A** u **C**
U single leader sistemima transakcije se redjaju jedna za drugom. Tako da ce se obaviti prva transakcija koja stigne, pa zatim druga.
Za multi leader sisteme situacija je slozenija:
- **Conflcit avoidance**: upisi za isti dokument idu na istog leader-a.
- **Converging towards consistent state**: u trenutnoj situaciji u multi leader sistemu u data centru 1 imas upisano **B** a u data centru 2 imas upisano **C** sto naravno nije prihvatljvo stanje stvari. Svakom write-u pridruziti **timestamp** ili **UUID** ili **random number** ili **key and value hash**. Izabrati onaj sa najvecom vrijednoscu i odbaciti ostale. Moguce je jos:
  - Pridruziti replikama neke ID-eve pa odrediti prioritete
  - Sacuvati podatke u nekoj strukturi pa rjesvati konflikte kasnije (ili rucno korisnici sami) kao git
  - Pokusati na neki smislen nacin da se razrijese konflikti - npr. naslov da bude B/C
- Posotje i algoritmi za automatsko razrjesavanje konflikata ali nisu jos integrisani u DBMS sisteme.
### Multi Leader replication topologies
Tri glavne topologije postoje:
- Circular (Kruzna) - MySQL podrzava samo ovu
- Star (Zvijezda)
- All-to-all (Svaki sa svakim)
Problem sa kruznom i zvijezda topologijom je to sto ako jedan node fail-uje onda se citav lanac replikacije prekida i obicno mora rucno da se rjesava. Svaki sa svakim rjesava taj problem ali tu postoji problem zbog potencijalnog kasnjenja prilikom replikacije.


## Leaderless replicaiton
Moze da se upisuje u bilo koju repliku. Amazon Dynamo, Cassandra, Vodlemort koriste leaderless replikaciju.
Upisuje se zapravo u vise replika i cita se iz vise replika. Podaci se verzionisu i tako se utvrdjuje koji su podaci azurni. Npr. ako podatak nije upisan u neku repliku jer je bila down.
Opet mora da se odrzava konzistento stanje u svim replikama:
- Read repair klijent pri citanju cita iz vise replika, ako ustanovi da je naka replika out of date, salje zahtjev za upis u tu repliku.
- Anti-entropy process - background process koji prolazi kroz sve replike i azurira bajate podatke.
### Quorums for reading and writing
Koliko replika treba citati i u koliko treba upisivati podatke?
n - ukupan broj replika
w - broj write replika
r - broj read replika
`w + r > n`
Ova formula ne garantuje da se nece citati stale vrijednosti (moguce je da nastane edge case u kome se to desi) ali je dobro pravilo.
### Monitoring staleness
Za leader based sisteme moze da se prati replication lag. Mjeri se tako sto se oduzme follower-ova pozicija u **replication log**-u od follower-ove. Za leaderless je to tesko izvesti. Postoje neki nacini da se izracunaju na osnovu w, r i n parametara.
### Sloppy quorum and hinted handoff
Sta raditi ako je dostupno manje node-ova (replika) od **w** ili **r**?
Da li vratiti greske svim klijentima koji ne mogu da postignu kvorum ili upisati podatak u dostupne node-ove?
Ako se odlucimo za upisivanje podataka a nije nam dostupno **w** node-ova koji su oznaceni kao **home** node-ovi za tu **vrijednost** onda se to zove **sloppy quorum**. Kada home cvorovi opet postanu dostupni onda se u njih upisuju vrijednosti i to se zove **hinted handoff**
### Last write wins
Izabere se onaj sa najvecim timestampom. Losa opcija ako nam je cilj da sacuvamo svaki write.
**Concurent** operacijom se smatraju one koje se izvrsavaju nad istim podacima od razlicitih procesa be za ti procesi znaju jedan za drugi. Ne moraju nuzno da se izvrsavaju u isto vrijeme.
Vazan sistem je verzionisanje podataka. Takodje prilikom brisanja nije dovoljno obrisati podatak iz takve baze vec markirati podatak kao obrisan - **tombstone** marker.