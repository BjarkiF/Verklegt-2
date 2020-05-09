#!/usr/bin/env bash
# Jóhann Berentsson
# Dump all rows in the database into a file.
pg_dump --cluster 12/main \
        -d uebfjgpj \
        -h 13.53.140.116 \
        -U uebfjgpj 
        -p 5432 
        -W 
        --data-only 
        --column-inserts > captain_console_data.database
