#!/usr/bin/env bash

S3_BUCKET="leasyfi-erpnext-backup"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BACKUP_DIR="/tmp"
BACKUP_FILENAME="db_${TIMESTAMP}.sql"
MEDIA_DIR="/home/erpnext/frappe-bench/sites/erp.leasyfi.com/public/files"

# Perform database backup
mariadb-dump --all-databases > "$BACKUP_DIR/$BACKUP_FILENAME"

# Check if backup succeeded
if [ $? -eq 0 ]; then
    echo "Database backup successfully created: $BACKUP_DIR/$BACKUP_FILENAME"
else
    echo "Error: Failed to create database backup"
    exit 1
fi

# Upload backup to S3
aws s3 cp "$BACKUP_DIR/$BACKUP_FILENAME" "s3://$S3_BUCKET/$S3_PREFIX$BACKUP_FILENAME"
aws s3 sync --size-only $MEDIA_DIR "s3://$S3_BUCKET/files/"


# Check if upload succeeded
if [ $? -eq 0 ]; then
    echo "Backup successfully uploaded to S3"
else
    echo "Error: Failed to upload backup to S3"
    exit 1
fi

# Clean up local backup file
rm "$BACKUP_DIR/$BACKUP_FILENAME"

echo "Backup process completed"
