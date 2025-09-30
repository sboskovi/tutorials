# React opet

## Kljucni koncepti
- ===
- !==
- Components
- Komponente su organizovane u tree (stablo). Key-evi identifikuju komponente u stablu, ako se promjeni key izmedju re render-a, react ce da smatra da je to nova komponenta. Zato nije dobra ideja imati random() vrijednosit za kljuceve
- props
- state - koristi se za cuvanje stanja komponente - svaka promjena state-a izaziva re-render. Treba cuvti samo neophodne podatke. Ono sto moze da se izracuna u funkciji (tijelu komponente) racunati u funkciji. 
- hooks - useState, useEffect.
- pure components:
  - Minds its own business (no side effects)
  - Same inputs, same output (idempotency)
- Skracenica za ternani op: `ternary ? ternary : null -> ternary ?? null`
- Array.slice lets you copy an array or a part of it.
- Array.splice mutates the array (to insert or delete items).
- Local storage:
```
localStorage.setItem("myCat", "Tom");
const cat = localStorage.getItem("myCat");
localStorage.removeItem("myCat");
localStorage.clear();
```
- `if (typeof window !== 'undefined')` // Check if we're running in the browser. - da se kod izvrsi samo jednom u **strict** mode-u


## key prop
- Dodjeljivanje <li> elementima - elementi liste
- Dodjeljivanje React komponentama - da React zna koja je komponenta u UI tree-u, zbog mount-ovanja i render-ovanja i cuvanja state-a i reset state-a
- Mozes **istoj** komponenti da proslijedis **razlicit kljuc** da joj **reset-ujes state** - bolje tako nego useEffect



## Props and state
- State is reserved only for interactivity
- DRY (Don't repeat yourself) - minimal representation stored in state, calculate everything else
- Objekti i nizovi, ne mjenjaj pojedinacne objekte vec pravi copy objekta setMyObject({...myObject, property: event.target.value})
- As a rule of thumb, if you want to **preserve the state between re-renders**, the structure of your tree needs to **match up** from one render to another. If the structure is different, the state gets destroyed because React destroys state when it removes a component from the tree.
-**key** treba da bude isti izmedju re-render-a da bi se ne bi ponovo rerender-ovali ako nema potrebe

## Refs
- const ref = useRef(initialValue);
- updating ref doesn't cause a re-render (updating state does)
- Don’t read or write ref.current **during rendering**
- the most common use case for a ref is to access a **DOM** element
- In general, you don’t want to access refs **during rendering**. That goes for refs holding DOM nodes as well. During the **first render**, the DOM nodes have not yet been created, so **ref.current will be null**. And during the rendering of updates, the DOM nodes **haven’t been updated yet**. So it’s too early to read them.

## Effects
- Svrha je da se koriste za **sinhonizacju sa nekim drugim sistemom**
- **Ne** koristiti za:
  - Pripremu (obradu) podataka za rendereovanje - state / props
  - Handlovanje korisnickih event-a (akcija)
- Izvrsavaju se nakon sto se komponenta **komitujue**
```
// Izvrsava se prilikom svakog rendera
useEffect(() => {})

// Izvrsava se samo na prvi render (mount)
useEffect(() => {}, [])

// Izvrsava se na mount i kada se a i b promjene
useEffect(() => {}, [a, b])
```
- Niz dependency-a mora da sadrzi dependency-e koji se koriste u useEffect
- U dependency-e stavljas samo **state** promjenljive, ne moras **ref** 
```
useEffect(() => {
  const connection = createConnection();
  connection.connect();
  return () => {
    connection.disconnect();
  };
}, []);
```

- How to handle the Effect **firing twice** in development? React intentionally remounts your components in **development** to find bugs like in the last example. The right question isn’t “how to run an Effect once”, but “how to fix my Effect so that it works **after remounting**”.



# Pitanja?

- when to use use state vs use ref
- Angular vs React
- why use portals?