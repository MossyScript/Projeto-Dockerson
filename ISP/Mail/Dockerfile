FROM ubuntu:latest

RUN apt-get update 
RUN apt-get install -y postfix dovecot-core dovecot-imapd 

COPY main.cf /etc/postfix/main.cf

COPY dovecot.conf /etc/dovecot/dovecot.conf

COPY 10-mail.conf /etc/dovecot/conf.d/10-mail.conf
COPY 10-auth.conf /etc/dovecot/conf.d/10-auth.conf
COPY 10-master.conf /etc/dovecot/conf.d/10-master.conf

COPY init.sh /init.sh
RUN chmod +x /init.sh

ENTRYPOINT ["/init.sh"]