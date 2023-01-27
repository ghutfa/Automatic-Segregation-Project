import os
import shutil
source = "C102_assets-main/C102_assets-main"
destination = "destination"
storage = os.listdir(source)
for i in storage:
    name , ext  = os.path.splitext(i) 
    if ext == "":
        continue
    if ext in ['.txt','.pdf']:
        path1 = source + "/" + i
        path2 = destination + "/" + "text_file"
        path3 = destination + "/" + "text_file" + "/" + i

        if(os.path.exists(path2)):
            print("moving the file...")
            shutil.move(path1, path3)
        else:
            print("creating path...")
            os.makedirs(path2)
            shutil.move(path1,path3)


