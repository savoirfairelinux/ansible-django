#!/bin/bash
mysql -u {{ django_dbuser }} --password="{{ django_dbpass }}" -e 'drop database {{ django_dbname }}; create database {{ django_dbname }};'
mysql -u {{ django_dbuser }} --password="{{ django_dbpass }}" -D {{ django_dbname }} 
