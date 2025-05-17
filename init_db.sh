#!/bin/bash
psql -d zyquests_db -f database/setup/01_init_tables.sql
psql -d zyquests_db -f database/setup/02_supply_tables.sql