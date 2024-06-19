#!/bin/bash
DATE=$(date +%Y%m%d-%H%M%S)
BACKUP_FILE=/root/backups/db-$DATE.sql.gz
/usr/bin/docker exec -it postgres pg_dumpall -U ruben | gzip -9c > $BACKUP_FILE
echo "Backup $BACKUP_FILE erstellt" >> /root/backup.log
