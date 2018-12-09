import sys
import glob
import urllib.request
import os

if len(sys.argv) != 3:
    print("run: python3 download.py http://file.csv.gz /path/to/save/");
    exit()

temp_folder = sys.argv[2]
filename = sys.argv[1]
savefile = temp_folder+os.path.basename(filename)

try:
    urllib.request.urlretrieve(filename, savefile)
except:
    print("File NOT downloaded")
    exit()

print("File downloaded")
os.system("gzip -d "+savefile)

basefilename = os.path.basename(savefile).replace('.gz', '')
csvfile = basefilename

print("extracted:"+temp_folder+csvfile)
