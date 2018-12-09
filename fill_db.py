import pymysql
import urllib.request
import os
import glob
import csv
from datetime import datetime
import sys

import warnings
warnings.filterwarnings('ignore', category=pymysql.Warning)

#settings
db_host = 'localhost' # DB HOST
db_user = 'root' # DB USER
db_password = '1' # DB PASSWORD

db_name = 'test_db' #DB NAME
db_table_name = 'domains' # TABLE NAME

db = pymysql.connect(db_host, db_user, db_password,local_infile=True)
cursor = db.cursor()



if len(sys.argv) != 2:
    print("run: python3 fill_db.py /path/to/csv/file.csv");
    exit()

csv_file = sys.argv[1]

#create the database and table
cursor.execute("CREATE DATABASE IF NOT EXISTS "+db_name)

create_table = 'CREATE TABLE IF NOT EXISTS '+db_name+'.'+db_table_name+' (domain text NOT NULL,   first_seen DATE NOT NULL, last_seen DATE NOT NULL, etld text NOT NULL, id int(11) NOT NULL,time_date_imported TIMESTAMP DEFAULT CURRENT_TIMESTAMP, primary key (id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;'

cursor.execute(create_table)

upload = "load data local infile '"+csv_file+"' REPLACE into table "+db_name+"."+db_table_name+" fields terminated by ',' "+'IGNORE 1 LINES (domain,@fs,@ls,etld,id,time_date_imported) SET first_seen=FROM_UNIXTIME(@fs), last_seen=FROM_UNIXTIME(@ls);'


cursor.execute(upload)

db.commit()
print("Done")




