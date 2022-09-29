import os
import shutil

from_dir = "C:/Users/nkann/Downloads"
to_dir = "C:/Users/nkann/OneDrive/Desktop/test"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extn = os.path.splitext(file_name)
    print(name)
    print(extn)
    
    if extn == "":
        continue

    if extn in [".gif" , ".png" , ".jpg" , ".jpeg" , ".jfif"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "image_files"
        path3 = to_dir + "/" + "image_files" + "/" + file_name

        print("path1" , path1)
        print("path3" , path3)

        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Making directory...")
            print("Moving" + file_name + "...")
            shutil.move(path1, path3)

    


