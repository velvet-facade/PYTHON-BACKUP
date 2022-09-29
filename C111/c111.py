import os
import shutil
source = "C:/Users/nkann/Downloads/11D.ipynb - Colaboratory.pdf"
destination = "C:/Users/nkann/OneDrive/Desktop/Ananya Kannan"
shutil.copy(source, destination)
print(os.listdir(destination))