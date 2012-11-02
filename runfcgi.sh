#!/bin/bash

PROJDIR=~+
PIDFILE="$PROJDIR/fcgi/ppp.pid"
SOCKET="$PROJDIR/fcgi/ppp.sock"

cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi


source ~/virtualenvs/photoparticipatio/bin/activate
python manage.py runfcgi socket=$SOCKET pidfile=$PIDFILE method=prefork daemonize=true umask=007

chmod 0777 $SOCKET

echo 'Готово!'