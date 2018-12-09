##requirements: pymysql (sudo pip3 install pymysql)

## 1. download.py download the archive and extracts 1 CSV file
### use:python3 download.py http://site.com/file.csv.gz /path/to/save/
## 2. fill_db.py created database and the table, fills(or updates) the table with CSV file.
### edit database settings in fill_db.py
###use:python3 fill_db.py /path/to/csv/file.csv
