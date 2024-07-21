FROM node:latest

WORKDIR /app

COPY package.json /app/package.json

RUN npm install --save

COPY server.js ./

EXPOSE 8040

CMD [ "npm", "start" ]
