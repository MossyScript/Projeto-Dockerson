# clients/client1/hotsite/Dockerfile
FROM nginx:alpine

# Remove o conteúdo padrão do Nginx
RUN rm -rf /etc/nginx/conf.d/* /usr/share/nginx/html/*

# Copia o conteúdo da pasta 'hotsite' (onde este Dockerfile está) para o diretório padrão do Nginx
COPY . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]