FROM node:12-alpine

WORKDIR /code

# copia dependencias
COPY ["package*.json", "/code/"]

# instala dependencias
RUN npm install

COPY [".", "/code/"]

EXPOSE 3000

CMD ["node", "./scripts/start.js"]
