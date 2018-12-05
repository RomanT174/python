import pymysql
import urllib.request
import os
import glob
import csv
from datetime import datetime
import sys

#settings
db_host = 'localhost' # DB HOST
db_user = 'root' # DB USER
db_password = '1' # DB PASSWORD

db_name = 'test_db1' #DB NAME
db_table_name = 'domains' # TABLE NAME

db = pymysql.connect(db_host, db_user, db_password)
cursor = db.cursor()



if len(sys.argv) != 2:
    print("run: python3 fill_db.py /path/to/csv/file.csv");
    exit()

csv_file = sys.argv[1]

#create the database and table
cursor.execute("CREATE DATABASE IF NOT EXISTS "+db_name)

create_table = 'CREATE TABLE IF NOT EXISTS '+db_name+'.'+db_table_name+' (domain text NOT NULL,  first_seen int(11) NOT NULL, last_seen int(11)NOT NULL, etld text NOT NULL, id int(11) NOT NULL,time_date_imported TIMESTAMP DEFAULT CURRENT_TIMESTAMP, primary key (id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;'

cursor.execute(create_table)

upload = "load data local infile '"+csv_file+"'REPLACE into table "+db_name+'.'+db_table_name+" fields terminated by ',' enclosed by '\"' lines terminated by '\n' IGNORE 1 LINES;"
cursor.execute(create_table)

print("Done")




