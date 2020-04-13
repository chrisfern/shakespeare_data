import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import shutil
from string import ascii_letters
import sys
from nltk.util import ngrams



def remove_extras(text):
    new_text=""
    for symbol in text:
        
        if symbol in ["\\","'",",","\"","{","}","%","*","|"]:
            new_text+=""
        else:
            new_text+=symbol
            
    return new_text

def make_dataset(text):
    first_edit=text[1:len(text)-1]

    dataset=[]
    word=""
    
    for symbol in first_edit:
        if symbol is " ":
            
            story.append(word)
            word=""
            
        elif symbol.isalpha():
            word+=symbol  

        if symbol is "[" :
            story=[]
           
        if symbol is "]":
            dataset.append(story)
       
        
    return dataset




file=open(sys.argv[1])
text=file.read()

edit_text=remove_extras(text)
datasetword=make_dataset(edit_text)
dataset=[]
for story in datasetword:
    fivegrams=ngrams(story,3)
    dataset.append(list(fivegrams))
    

#dataset=[["a","b","c"],["b"],["b","c"]]
te=TransactionEncoder()
te_ary=te.fit(dataset).transform(dataset)
df=pd.DataFrame(te_ary,columns=te.columns_)
#print(df)


print("about to start 1")
frequent_itemsets=apriori(df, min_support=0.6, use_colnames=True)

frequent_itemsets['length']=frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets=frequent_itemsets.sort_values(by='support')

print("about to start 2")


print(frequent_itemsets)