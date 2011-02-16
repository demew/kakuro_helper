#!/usr/local/bin/bash

# This script resets & populates the kakuro database.

mysql -u janedoe --password=xxxxxxxx -h localhost < init/kakuro_table_init.sql 

python init/kakuro_table_populate.py
