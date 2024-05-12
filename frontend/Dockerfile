FROM node:21-alpine

WORKDIR /sin_renderer

COPY package.json ./
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
