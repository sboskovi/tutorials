FROM node

WORKDIR app/

COPY package.json .

RUN npm install --save-dev

COPY . .

ENV MONGO_USER=admin

ENV MONGO_PASSWORD=root

EXPOSE 80

CMD ["npm", "start"]

