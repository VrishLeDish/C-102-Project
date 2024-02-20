import os
import shutil
from_dir = "C:/Users/vrish_fl8o8kc/Downloads/ABCD"
to_dir = "C:/Users/vrish_fl8o8kc/Documents"
list_of_files = os.listdir(from_dir)
#print(list_of_files)

for d in list_of_files:
    name,ext = os.path.splitext(d)

    if ext == "":
        continue 
    if ext in [".gif",".png",".jpg",".jpeg",".gfif"]:
        path1 = from_dir + "/" + d
        path2 = to_dir + "/" + "Documents_Files"
        path3 = to_dir + "/" + "Documents_files" + "/" + d

        if os.path.exists(path2):
            print("This Folder Exists And Moving The Files")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Creating The New Folder And Moving The Files")
            shutil.move(path1,path3)

