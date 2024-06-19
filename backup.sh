#!/bin/bash
DATE=$(date +%Y%m%d-%H%M%S)
/usr/bin/docker exec -it postgres pg_dumpall -U ruben | gzip -9c > /root/db-$DATE.sql.gz
echo "Backup db-$DATE.sql.gz erstellt" >> /root/backup.log
