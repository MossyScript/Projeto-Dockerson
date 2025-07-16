#!/bin/sh
# Verifica se os Maildirs já existem no volume, se não, copia do backup interno
if [ ! -d "/home/dockerson/Maildir" ];      then
    cp -r /maildata/dockerson /home/
fi

if [ ! -d "/home/kuberneterson/Maildir" ];  then
    cp -r /maildata/kuberneterson /home/
fi

if [ ! -d "/home/dnsilson/Maildir" ];       then
    cp -r /maildata/dnsilson /home/
fi

chown -R dockerson:dockerson            /home/dockerson
chown -R kuberneterson:kuberneterson    /home/kuberneterson
chown -R dnsilson:dnsilson              /home/dnsilson

# Iniciar serviços
service syslog-ng start
service dovecot start
service postfix start

# Manter container rodando
tail -f /dev/null