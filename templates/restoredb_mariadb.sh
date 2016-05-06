#!/bin/bash
mysql -u {{ django_dbuser }} --password="{{ django_dbpass }}" -D {{ django_dbname }} 
