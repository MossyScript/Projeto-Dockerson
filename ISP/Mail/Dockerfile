FROM ubuntu:latest

RUN apt-get update 
RUN apt-get install -y postfix dovecot-imapd dovecot-pop3d syslog-ng

COPY main.cf /etc/postfix/main.cf

RUN service postfix start
RUN service dovecot start

CMD ["tail", "-f", "/dev/null"]