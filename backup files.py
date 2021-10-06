import time
import os
import shutil

path = input("Enter the file name")
ti = time.time()
os.path.exists(path)
path = path + '/'
ctime = os.stat(path).st_ctime
return ctime
