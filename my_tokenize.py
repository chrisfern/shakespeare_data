import shutil
import sys
import nltk
from nltk.tokenize import word_tokenize
import os
from os import walk
import pickle



file_list=[]

for(dirpath,dirnames,filenames) in walk("./"):
        file_list.extend(filenames)

shakespeare_words_set=[]

for files in file_list:
    file=open(files)
    text=file.read()
    
    shakespeare_words_set.append(word_tokenize(text=text))

new_file=open("../../../shakespeare_word_set","w+")

new_file.write(str(shakespeare_words_set))

new_file.close()

