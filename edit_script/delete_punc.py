import shutil
from os import walk
import os

def get_files():
    file_list=[]
    txt_list=[]

    for(dirpath,dirnames,filenames) in walk("./"):
        file_list.extend(filenames)
       
    for name in file_list:
        if "no_punc" in name:
            txt_list.append(name)

    return txt_list

for name in get_files():
    os.remove(name)
