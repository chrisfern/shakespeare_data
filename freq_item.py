import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

from mlxtend.frequent_patterns import apriori
import shutil
from string import ascii_letters
import sys



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
            if all(c in ascii_letters or c in ["]","]"," "] for c in symbol):
                story.append(word)
            word=""
            
        else:
            word+=symbol  

        if symbol is "[":
            story=[]
        if symbol is "]":
            dataset.append(story)
        
        
        
    return dataset




file=open(sys.argv[1])
text=file.read()

edit_text=remove_extras(text)
dataset=make_dataset(edit_text)

print(len(dataset[0]))

te=TransactionEncoder()
te_ary=te.fit(dataset).transform(dataset)
df=pd.DataFrame(te_ary,columns=te.columns_)
print(df.shape)

print("about to start 1")
frequent_itemsets, rules=apriori(df[1:2], min_support=1)

#print("about to start 2")
#frequent_itemsets['length']=frequent_itemsets['itemsets'].apply(lambda x: len(x))

#print(frequent_itemset