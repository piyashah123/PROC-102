# program for file seggregation 
import os
import shutil
from_dir='D:/Downloads'
to_dir='D:/Downloads/images'
list_of_files= os.listdir(from_dir)
print(list_of_files)
# move all file from download folder to other
for file_name in list_of_files:
   name,extension=os.path.splitext(file_name)
   print(name)
   print(extension)
   if extension=="":
   continue

 