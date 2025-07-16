
FROM nginx:alpine

RUN rm -rf /etc/nginx/conf.d/* /usr/share/nginx/html/*

COPY . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]