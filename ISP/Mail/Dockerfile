FROM ubuntu:latest

RUN apt-get update 
RUN apt-get install -y postfix dovecot-core dovecot-imapd 

#COPY main.cf /etc/postfix/main.cf

#RUN service postfix start
#RUN service dovecot start

CMD ["tail", "-f", "/dev/null"]