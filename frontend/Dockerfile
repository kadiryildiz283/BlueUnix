# GÜNCELLENDİ: Node 18 yerine Node 22
FROM node:22-alpine

WORKDIR /app

COPY package.json .

# Bağımlılıkları yükle
RUN npm install

COPY . .

# Vite sunucusunu dış ağa aç
CMD ["npm", "run", "dev", "--", "--host"]
