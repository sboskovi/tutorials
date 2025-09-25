# CSS course

### Ordering classes in css file
Ovo ima efekta na primjenjene stilove, ako dvije klase definisu isti property za isti element, npr `color`, primjenice se onaj koji je kasnije definisan. Nema veze kojim redom se navedu klase u HTML `class` atributu.

### CSS Margin collapsing
Uvijek se bira margina sa vecom velicinom izmedju dva (?block level?) elementa i primjenjuje se samo ona!

### Block VS Inline
Block zauzimaju sav dostupan horiznotalni prostor.
Inline elemetni zauzimaju samo neophodan prostor za prikazivanje sadrzaja. Margina gore i dole, width i height nemaju efekta. Padding gore i dole se drugacije ponasaju.
Block elementi: `<div>, <section>, <article>, <nav>, <h1>, <h2>, <p>`
Inline elementi: `<a>, <span>, <img>`

### Combinators
`>` diretkni potomak html elementa. npr. `.my-style > div` 
`+` za element koji prati direktno ovaj. `.p1 + p`



### Position
The **viewport** is the user's visible area of a web page. Dio stranice koju korisnik vidi.

**Pozicioni kontekst** se moze promijeniti ako se roditeljskoj komponenti setuje position razlicit od `static`.
**Top**, **right**, **bottom** i **left** odredjuje pozicioniranje u odnosu na pozicioni kontekst.
Za `fixed` i `absolute` position elemetni se izbacuju iz document flow-a. 
Za `fixed` pozicioni kontekst je **viewport**.
Za `absolute`pozicioni kontekst je **roditeljski** element koji ima setovan position razlicito od static ili na **html** element ako ni jedan roditeljski nema.
Za `relative` se ne izbacuju iz document flow-a. Top, right, bottom i left se odnosi **inicijalnu** poziciju.
`overflow: hidden` u roditeljskoj komponenti da se child komponente sa `relative` sakriju ako izadju van roditeljske komponente.
Za `sticky` je **viweport** i jos neki element.

### Z index
Ako 2 elementa imaju isti z index (i postavljen je position na nesto razlicito od default-nog `static`) onda ce element koji se nalazi kasnije u html kodu (ispod prvog) biti prikazan preko prvog
Z index se promjenjuje untar **stacking context**-a. Svaki element ima svoj stacking context i primjenjuje se na child komponente, tako da child komponenta sa vecim 
z-index-om od neke komponente koja sibling roditeljskoj komponenti ne moze da prekrije *strica*.

### Images
`width/height: 100%` se odnosi na samu sliku ako je okolni element inline `<a>`. Ako je `inline-block` (blok element) onda se odnosi na velicinu okolnog elementa


# Sizes and units

### %
% zavisi od position property elemnta i odredjuje velicinu proceuntalno u odnosnu na `containing block`.
Za `fixed`, `containing block` je viewport
Za `absolute`, `containing block` je roditeljski element koji nije position `static`. % racnua i padding roditeljskog elementa. Ako nema roditeljekog elemnta sa position prop-om, onda gleda **viewport**
Za `relative` ili `static`, `containing block` je roditljski element koji je **block level** element. Ne ukljucuje padding u %
Za relative ili static **height 100%** moze da se setuje samo ako je roditeljskim elementima setovan height 100%. Ili je bolje koristiti fixed


### em i rem
Velicina zavisi od velicine fonta koja je podesena u browser-u.
`em` se racuna kao kombinacija svih nasljedjenih velicina fontova iz roditlejskih komponenti. 2em pa child-u 2em daje 4em (em je velicina koju definise browser, npr 16px)
`rem` root em - ne radi stekovanje svih velicna fontova vec samo root-a - <html>.


### vw i vh
Se odnose na `viewport` i brojevi su u procentima
`vmin` u odnosu na manju osu `viewport`-a (sirina ili visina)
`vmax` u odnosu na siru osu `viewport`-a

### Kako izabrati velicine
- `font size` - rem
- `margins` / `padding` - rem ili px ako hoces fiksne
- `border` - px
- `width` / `height` -  % ili vw, vh u zavisnosti od situacije
- `max-width` / `max-height` - moze i u px
- `top` / `bottom`, `left` / `right` - %

### margin:auto
Radi samo za `block level` elemente kojima je setovan `width` property.


# Flexbox
```
flex-direction: row  | flex-direction: column
---> MAIN axis	       ---> CROSS axis
|                      |
|                      |
|                      |
v                      v
CROSS axis             MAIN axis
```

```
flex-direction: row / column; row-reverse / column-reverse
flex-wrap: nowrap / wrap;
align-items: center / flex-(start / end) / ; /* align items along **CROSS** axis */
justify-content: center / flex-(start / end) / space-between  /* align items along **MAIN** axis*/ `justify-content: baseline` /* align items to the baseline of the content  */
align-content: /* for multi line flexboxes. Aligns multiple lines on **CROSS** axis */
```

### Child flex-box properties
self-align: center, ... - u odnosu na flex-container
flex-grow: 0  - da ne raste prilikom promjene sirine / visine. flex-grow se racuna procentualno u odnosu na citav flex container i svih flex-grow vrijednosit medju flexbox children-ima
flex-basis - u odnosu na **MAIN** aixs
order: 0; - default, sve razlicito od toga se koristi za pozicioniranje


# CSS Grid
```
display: grid;
```
Na elemente koji nisu dio document flow-a (postion: fixed / relative...) ne djeluje display: grid;

## Grid
grid-template-columns: repeat(4, 25%);
grid-template-rows: [row-1-start ] 5rem minmax(10px, auto) [row-1-end row-2-start] 100px;

// U girdu:
grid-template-columns: repeat(4, [col-start] 25% [col-end]);
// U child-u da pozicinoiramo element u drugu kolonu
grid-column: col-start 2 / col-end 2;

### named tempalate areas
Moze da se koristi kao zamjena za pojedinacni span u child-ovima

Mora da definise template koji se pravi preko `grid-template-*`. U ovom slucaju: 4 kolone i 3 reda. Header zauzima sve 4 kolone, side i main po 2 kolone i footer zauzima 4.

`.` moze da se koristi da kolona ne ostane prazna. Npr zamijenimo side sa: . .
```
grid-template-areas: "header header header header"
					 "side side main main" 
					 "footer footer footer footer";
```
U child-u:
grid-area: header;


### fit-content
// Treca kolona zauzima min 8rem ili vise dok ne fituje content
grid-template-rows: 3rem auto fit-content(8rem);


### jusitfy-items
// Positions grid elements within grid-element **cell**
justify-items: strech;

### justify-content
// Positions entire grid within grid cell along **X** axis
### align-content
// Positions entire grid within grid cell along **Y** axis

### Grid auto flow
grid-auto-rows: minmax(8rem, auto);
grid-auto-flow: column;


### auto-fill
// Popunjava trenutni red koliko je moguce, pa onda prelazi u novi red
// Ako hoces da ogranicis max broj elemata mozes da setujes `max-width`
grid-template-columns: repeat(auto-fill, 10rem);

### auto-fit
// Isto kao auto-fill, samo centrira elemente
grid-template-columns: repeat(auto-fit, 10rem);




## Grid elements (CHILDREN)
grid-column-start: 1;
grid-column-end: span 2;

### span
grid-column: span 2

### shorthends
// start / end
grid-column: 1 / -1;
// row / col ....
grid area: row-1-start / col-3-end / row-2-end / span 3;

### gaps
grid-column-gap: 20px;
grid-row-gap: 10px;
// or
grid-gap: 20px 10px;

### justify-self
// along **X** axis
### align-self
// along **Y** axis


# Grid vs Flexbox
Grid
- dvodimenzionalno pozicioniranje - redovi i kolone
Flexbox
- jendodimenzionalno pozicioniranje - redovi ili kolone