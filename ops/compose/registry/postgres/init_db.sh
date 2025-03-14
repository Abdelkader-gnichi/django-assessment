#!/bin/bash
set -e


DB_NAME="photos_db"
if psql -U postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME'" | grep -q 1; then
  echo "Database $DB_NAME already exists"
else
  echo "Creating database $DB_NAME..."
  createdb -U postgres $DB_NAME
fi