# React course

## Osnovni koncepti
Osnovni elementi Ract-a su komponente. To su JS funkcije cije ime pocinje velikim slovom i koje vracaju `renderable` (JSX) sadrzaj.
```
fucntion Header(props) {
	return <h1>{props.my_title}</h1>
}
// ...
<Header my_title="Atribut naziv" />
```

### Passing the props
Object destructuring `const a,b,c = ..abc` se cesto koristi za props.
```
<TabButton id="examples" onClick={() => onSelect()}> ... </TabButton>
export default function TabButton({someProp, ...buttonProps}) {
	if (someProp) {
		....
	}
	return (
	<>
		<button {...buttonProps}> <button>
	</>
	)
}
```

### Children prop
`children` je rezervisan prop za ono sto ide izmedju tagova komponente. Npr
```
<MyComponent>This text is children</MyComponent>
```


### React HOOKS
useState i ostali hooks moraju se koristiti iz React komponente, i to u top level block-u, definiciji funkcije, ne moze cak ni unutar if-a.
```
function App() {
	const [val, setVal] = useState("My initial special value");
}
```
pozivanje setVal funckije zakazuje (schedule-uje) mijenjanje vrijednosti, nece biti izvrseno odmah.

### import image

```
import myImage from './assets/image.png'

// ...

<img src={myImage} />
```

### Fragments 
Used to return single element
```
<Fragment>
</Fragment>
or 
<>
</>
```

### Styling by id
```
// .css
# element h2 { ... }
// JS
<div id="element"></div>
```



### Setting component type dinamically
```
<Tabs buttonContainer="menu"> <!-- HTML menu-->
<Tabs buttonContainer=<Section>> <!-- React component Section -->
export default Tabs({...buttonContainer}) {
	// Because react components need uppercase letter
	const ButtonContainer = buttonContainer;
	return <>
		<ButtonContainer></ButtonContainer>
	</>
}
```

### Updating state based on previous state
Because state updates are not instant but scheduled, so state update function should be used.
```
setIsEditing((editing) => !editing);
```