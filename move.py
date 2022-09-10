import os
import shutil
import time
from_dir = "C:/Users/JISHNU D/Downloads/Org_Files"
to_dir = "C:/Users/JISHNU D/Desktop/C112Project_Ordered_files"

file_list = os.listdir(from_dir)

for file_name in file_list:

    name,ext = os.path.splitext(file_name)
    if(ext == ''):
        continue
    if(ext in [ '.txt', '.doc', '.docx', '.pdf']):
        path1 = from_dir +'/'+ file_name
        path2 = to_dir +'/'+ 'Text_Files'
        path3 = to_dir +'/'+ 'Text_Files'+'/'+file_name

        if(os.path.exists(path2)):
            print('Moving '+file_name+'...')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)          
            print('Moving '+file_name+'...')
            shutil.move(path1,path3)

    time.sleep(0.5)
