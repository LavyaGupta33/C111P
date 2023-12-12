import os
import shutil

from_dir ='C:/Users/lavya/Downloads/Downloads'
to_dir= 'C:/Users/lavya/OneDrive/Desktop/Document_Files'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file in list_of_files:
    name,extension =os.path.splitext(file)
    print(name)
    print(extension)

