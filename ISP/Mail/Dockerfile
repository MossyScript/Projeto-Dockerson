FROM ubuntu:latest

RUN apt update --fix-missing -y
RUN apt upgrade -y
RUN apt-get install -y postfix dovecot-core dovecot-imapd syslog-ng

RUN useradd -m -s /bin/bash dockerson       && \
    echo "dockerson:senha" | chpasswd

RUN useradd -m -s /bin/bash kuberneterson   && \
    echo "kuberneterson:senha" | chpasswd

RUN useradd -m -s /bin/bash dnsilson        && \
    echo "dnsilson:senha" | chpasswd

RUN mkdir -p /maildata/dockerson/Maildir    /maildata/kuberneterson/Maildir /maildata/dnsilson/Maildir && \
    chown -R dockerson:dockerson            /maildata/dockerson && \
    chown -R kuberneterson:kuberneterson    /maildata/kuberneterson && \
    chown -R dnsilson:dnsilson              /maildata/dnsilson && \
    chmod -R 700                            /maildata/*


COPY ./config/main.cf /etc/postfix/main.cf

COPY ./config/dovecot.conf   /etc/dovecot/dovecot.conf
COPY ./config/10-mail.conf   /etc/dovecot/conf.d/10-mail.conf
COPY ./config/10-auth.conf   /etc/dovecot/conf.d/10-auth.conf
COPY ./config/10-master.conf /etc/dovecot/conf.d/10-master.conf

COPY init.sh /tmp/init.sh
RUN chmod +x /tmp/init.sh

ENTRYPOINT [ "/tmp/init.sh" ]

