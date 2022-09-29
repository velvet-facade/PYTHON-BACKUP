import os
import shutil

from_dir = "C:/Users/nkann/Downloads"
to_dir = "C:/Users/nkann/OneDrive/Desktop/test"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    os.path.splitext(list_of_files)
