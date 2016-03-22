#!/bin/bash
mysqldump -u {{ django_dbuser }} --password="{{ django_dbpass }}" {{ django_dbname }} 
