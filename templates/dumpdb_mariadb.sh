#!/bin/bash
mysqldump -u {{ django_dbuser }} --password="{{ django_dbpass }}" -d {{ django_dbname }} 
