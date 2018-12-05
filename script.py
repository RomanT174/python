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
db_password = '' # DB PASSWORD

db_name = 'test_db' #DB NAME
db_table_name = 'domains' # TABLE NAME
temp_folder = '/tmp/temp/'; # EMPTY FOLDER FOR TEMP DATA (MUST BE WRITABLE)
###

db = pymysql.connect(db_host, db_user, db_password)
cursor = db.cursor()



if len(sys.argv) != 2:
    print("run: python3 script.py http://file.csv.gz");
    exit()

filename = sys.argv[1]

outfile = temp_folder+"file.csv.gz"

files = glob.glob(temp_folder+'*')
for f in files:
    os.remove(f)

try:
    urllib.request.urlretrieve(filename, outfile)
except:
    print("File NOT downloaded")
    exit()

print("File downloaded")
os.system("gzip -d "+outfile)

files = glob.glob(temp_folder+'*')
if (len(files) == 0):
    print("no files extracted")
    exit()

csvfile = files[0]

#create the database and table
cursor.execute("CREATE DATABASE IF NOT EXISTS "+db_name)

create_table = 'CREATE TABLE IF NOT EXISTS '+db_name+'.'+db_table_name+' ( id int(11) NOT NULL, domain text NOT NULL, first_seen date NOT NULL, last_seen date NOT NULL, etld text NOT NULL,time_date_imported date NOT NULL, primary key (id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;'

cursor.execute(create_table)

#filling the db
print("Filling the table")
reader = csv.DictReader(open(csvfile))
added = 0
for row in reader:
    field_id = int(row['id'])
    ts = int(row['first_seen'])
    first_seen = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO "+db_name+"."+db_table_name+" (id, domain, first_seen, last_seen, etld, time_date_imported ) VALUES (%s, %s, %s, %s, %s, NOW()) ON DUPLICATE KEY UPDATE domain = VALUES(domain), first_seen = VALUES(first_seen), last_seen = VALUES(first_seen), etld = VALUES(etld), time_date_imported = VALUES(time_date_imported)", (field_id, row['domain'], first_seen, first_seen, row['etld']) )
    db.commit()
    added += 1

print("Added "+str(added)+" domains")

files = glob.glob(temp_folder+'*')
for f in files:
    os.remove(f)


