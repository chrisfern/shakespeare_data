import shutil

from os import walk
import sys
from shutil import copy

def delete_punc(args):
    file = open(args,"r")
    text= file.read()
    
    new_name=args.replace(".txt","no_punc.txt")


    new_file=open(new_name,"w+")

    for symbol in text:
        if symbol not in [".",",",":",";","!","?","[","]","(",")"]:
            new_file.write(symbol)
            
    new_file.close()
    
    copy(new_name,"./edit_folder")
    return

def get_files():
    file_list=[]
    txt_list=[]

    for(dirpath,dirnames,filenames) in walk("./"):
        file_list.extend(filenames)
        break
    for name in file_list:
        if ".txt" in name:
            txt_list.append(name)

    return txt_list


    
   
        
    

for name in get_files():
    delete_punc(name)
 

