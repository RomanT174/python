import sys
import glob
import urllib.request
import os

if len(sys.argv) != 3:
    print("run: python3 download.py http://file.csv.gz /path/to/save/");
    exit()

temp_folder = sys.argv[2]
outfile = temp_folder+"file.csv.gz"
filename = sys.argv[1]

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

print("extracted:"+csvfile)
