# Dev build
# FROM node:alpine
#  
# WORKDIR /app
#  
# # Copy package.json and package-lock.json and install dependencies
# COPY package*.json ./
# RUN npm install
#  
# COPY . .
#  
# EXPOSE 3000
#  
# CMD ["npm", "run", "dev"]

FROM node:18-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build
 
# Prod
FROM nginx:stable-alpine AS production

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
