#!/bin/bash
export PGPASSWORD="{{ django_dbpass }}"
pg_dump -d {{ django_dbname }} -U {{ django_dbuser }} -h localhost
