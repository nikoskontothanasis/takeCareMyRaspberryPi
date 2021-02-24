#!/bin/bash

#
# This script requires the "jq" package to be installed.
# Linux: apt-get install jq
# macOS: brew install jq
#

set -e

# Uncomment to debug
# set -x

USERNAME=$1
PASSWORD=$2
UI_HOST=http://localhost:8581
BACKUP_FILE_PATH="$(pwd)"

BACKUP_FILE_NAME="backup-$(date '+%Y-%m-%d').tar.gz"

# Get Access Token
ACCESS_TOKEN=$(curl -fs "$UI_HOST/api/auth/login" \
    -H 'Content-Type: application/json' \
    --data-binary "{\"username\":\"$USERNAME\",\"password\":\"$PASSWORD\"}" \
  | jq -r .access_token)

# Download Backup
curl -fs "$UI_HOST/api/backup/download" \
  -H "Authorization: bearer $ACCESS_TOKEN" \
  -o "$BACKUP_FILE_PATH/$BACKUP_FILE_NAME"

echo "Backup saved to $BACKUP_FILE_PATH/$BACKUP_FILE_NAME"