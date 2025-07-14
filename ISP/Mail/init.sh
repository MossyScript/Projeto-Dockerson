#!/bin/sh

service syslog-ng start
service dovecot start
service postfix start

tail -F /var/log/mail.log