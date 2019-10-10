#!/bin/bash
mysqldump -u {{ django_dbuser }} --password="{{ django_dbpass }}" {{ mysqldump_extra_args }} --quick {{ django_dbname }}
