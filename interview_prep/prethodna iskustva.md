# Pricaj o iskustvima
Ispricaj sta si radio na projektima. Daj ljudima detalja o projektu da im bude jasno o cemu pricas.


## HX Renew
- Pravimo aktuarske modele, nisu tehnicki zahtjevni, nezgodna je organizacija projekta
- Oni nama prave spec-ove  u excel-u, mi na osnovu njih pravimo modele, i nalazimo bug-ove u specu
- Organizacija losa, i nije izazovno, samo je komplikovano


## FWWB
Radili smo za DL, oni prave docking statione. Radili smo na softveru za build-ovanje firmare image-a za docking statione.

### Tehnologije
- NextJs, React i NodeJs, MySQL i Sequelize

# Opis aplikacije
- Klijenti ili oni sami dodju i konfigurisu firmver kroz aplikaciju (old FWWB)
- 
- Izbildovani image-i, konfiugrisu se i generisu paketi koji se salju vendorima
- Check-outovanje citavog repozitorijuma na odredjenu granu, za odredjenu verziju za odredjeni chip i generisu se image-i
- Prvo kondezovati citav repozitorijum na jednu granu
- Uradjeno verzionisanje pojedinacnih deskriptora kako smo ih zvali - funkcionalsniti chip-a
- Zatim smo pravili aplikaciju koja omogucava konfigurisanje softvera za konfiguraciju novih chip-ova (i postojecih)
- Nama je zadatak bio da napravimo aplikaciju za konfigurisanje firwmware-a kroz graficki UI
- Aplikacija se sastojala od Konfiguratora i Admin panela - u kome je bilo moguce podesavati izgled i ponasanje stranice za odredjeni cip
- Krajnji korisnik podesava konfiguraciju chip-a, HDMI, VGA, koliko USB portova, neki protokoli itd.
- Admin korisnik definise kako krajni korisnik vidi, i kako moze da interaguje sa odredjenom stranicom / chip-om


## Mev-Kav
Aplikacija za prodaju Kaspersky licenci direktno jednom malom vednoru.

### Tehnologije
- Angular, NodeJs, Docker, Google Cloud, SOAP protokal za integraciju sa njihovim sistemima

### Opis aplikacije
- Proizvodi - SKU-ovi, Promo Kodovi
- 