#!/bin/bash
pg_dump -d {{ django_dbname }}
