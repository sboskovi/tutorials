# NodeJS course
NodeJS je JavaScript **runtime** koji omogucava da se JavaScript izvrsava na serveru. Tipicno se JavaScript izvrsava u browser-u i nema pristup lokalnim fajlovima zbog sigurnosnih
razloga, NodeJs prosiruje JS tim i jos nekim funkcionalnostima.
Single threaded, uses **event loop** to respond to requests. Event loop izvrsava **Event Callback**-ove. **Worker Pool** radi sa fajlovima npr, zasebne niti u odnosu na
Event Loop.
Lekcije 36 do 39

- https://nodejs.org/en/learn/getting-started/introduction-to-nodejs
- https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick
- https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop

## Sync vs Async
Bolje je koristiti npr **writeFile** umjesto **writeFileSync** jer asinhrona verzija nece blokirati event loop dok se upisu podaci u fajl. 
Isto vazi za ostale blokirajuce stvari - pristup bazi npr.

# NodeJS basics
Server can be started with http module. Server will run as long as there are active listners.

```
const server = http.createServer((req, res) => {
	res.setHeader("Content-Type", "text/html");
	res.write("<html>");
	res.write("...");
	res.write("</html>");
	res.end();
});
server.listen(3000);

```

### Streams and buffers
Stream - request se stastoji od **chunk**-ova, tako da teoretski moze da se cita dio request-a i obradjuje.
Buffer - chunk-ovi se organizuju u buffer-e smislene cjeline (odredjeni broj chunk-ova) koje mozes da obradjujes
```
const body = [];
// Register listener to listen to data event
request.on('data', (chunk) => {
	body.push(chunk);
});
// Register listener once all chunks arrive
request.on('end', () => {
	const parsedBody = Buffer.concat(body).toString();
	fs.writeFile('otuput.txt', body, () => {});
});
```

# Debug
Moze da se koristi VS code debugger. **Debug console** moze da se koristi da se izvrsavaju komande u runtime-u. 
Mozes da koristis breakpoint-e, watch-eve, da mijenjas vrijednosti promjelnjivima ...

https://code.visualstudio.com/docs/nodejs/nodejs-debugging
https://nodejs.org/en/learn/getting-started/debugging

# Node Package Manager - NPM
- npm init
- npm install
- npm start
- npm run my-script
- npm install -g nodemon
- npm install --save-dev nodemon


# Express

```
const express = require("express");
const app = express();

# Use middleware
app.use((req, res, next) => {
	res.send(); // by default html
	res.json();
	next();
});

app.listen(3000);
```
Redoslijed middleware-a je bitan. Takodje je bitan **pathing!!!**

## BodyParser
Middleware koji se koristi da parsira tijelo request-a.
```
app.use(bodyParser.urlencoded({ extended: false }));
```


## Router
```
// routes/shop.js
const Router = express.Router();

router.get()
router.post()
router.use()

// app.js
const adminRoutes = rquire("./routes/admin");
const shopRoutes = require("./routes/shop");

app.use(adminRoutes);
app.use(shopRoutes);

```

# File access i Pathing
Treba izbjegavati putanje sa slash-evima zbog kompatabilnosti windows - linux. Bolje koristiti path.join nego hardkovati string putanje - `url/hello`
```
const path = require("path");

// Path to a project root directiory
rootDir = path.dirname(process.mainModule.filename);

res.sendFile(path.join(rootDir, "views", "shop.html"));
```
## Citanje i pisanje u fajlove
Velike fajlove treba citati kao stream. fs.createReadStream?

JSON.parse(fileContent);
JSON.stringify(products);

## Static files
```
app.use(express.static(path.join(rootDir, "public")));
```