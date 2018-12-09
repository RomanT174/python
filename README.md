<<<<<<< HEAD
##requirements: pymysql (sudo pip3 install pymysql)

## 1. download.py download the archive and extracts 1 CSV file
=======
## 1. download.py downloads the archive and extracts 1 CSV file
>>>>>>> e5fba58fc56c4644d4ba64eb4e03a682086f85da
### use:python3 download.py http://site.com/file.csv.gz /path/to/save/
## 2. fill_db.py creates database and table, fills(or updates) the table with CSV file.
### edit database settings in fill_db.py
###use:python3 fill_db.py /path/to/csv/file.csv
