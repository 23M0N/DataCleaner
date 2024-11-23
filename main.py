import pandas as pd
from spellchecker import spellchecker
from word2number import w2n
import numpy as np
       
#file_name = input("enter the file name that u want to clean : ")
df = pd.read_csv('test/Data.csv')
print(df.to_string())


print('starting by deleting duplicates raws')
df = df.drop_duplicates()


print('removing extra spaces')
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)



def getAnswer(mess):
    answer = input(mess)

    if answer in ['yes', 'YES', 'Yes', 'y'] :
        return True
    elif answer in ['no', 'NO', 'No', 'n'] :
        return False
    
    return False


def convert_to_number(value):
    try:
        return w2n.word_to_num(value)
    except:
        return np.nan


def noneValue(df, column): 
    df[column] = df[column].replace('Unknown', None)
    df = df.dropna(subset=[column])



def replacingChar(df, column):
    n = int(input("how many characters do you want to delete or replace : "))
    inputs = []
    for _ in range(n):
        value =  input('enter the character :')
        inputs.append(value)    
    choice = input("do you want to replace these characters or delete them (delete/replace) :")
    if choice == 'delete':
        for char in inputs:
            df[column] = df[column].apply(lambda x: str(x))
            df[column] = df[column].str.replace(char, '', regex=False)
    elif choice == 'replace':
        replace = input('replaced by what ? :')
        for char in inputs:
            df[column] = df[column].apply(lambda x: str(x))
            df[column] = df[column].str.replace(char, replace, regex=False)
    else:
        print('error')

    return df


def spelling(df, column):
    spell = spellchecker()
    df[column] = df[column].apply(lambda x: spell.correction(x))

    return df


def replacingEmptyCells(df, column):
    choice = input("by what do you want to replace these empty cells (median/mean) :") 
    if choice == 'median':
        df[column] = df[column].astype(str).apply(convert_to_number)
        noneValue(df, column)
        df[column] = df[column].fillna(df[column].median())
        df[column] = df[column].apply(lambda x: int(x))
    elif choice == 'mean':
        df[column] = df[column].astype(str).apply(convert_to_number)
        noneValue(df, column)
        df[column] = df[column].fillna(df[column].mean())
        df[column] = df[column].apply(lambda x: int(x))
    else:
        df[column] = df[column].fillna(choice)
    
    return df


column = df.shape[1]

for x in range(column):
    
    column = df.columns[x]
    answer = getAnswer('do you want to clean the column named :' +column +'(yes/no)')
    
    if answer:
        answer = getAnswer('do you want to replace or delete some characters (yes/no)')
        
        if answer:
            df = replacingChar(df, column)
        
        answer = getAnswer('do you want to delete an entire raw because of empty cells (yes/no)')
        
        if answer:
            df = df.dropna(subset=[column])
        
        elif not answer:
            answer = getAnswer('do you want to replace empty cells by something (yes/no)')
            
            if answer:
                df = replacingEmptyCells(df, column)

        #answer = getAnswer('do you want to correct spelling mistakes (yes/no)')
        #if answer:
            #df = spelling(df, column)

print(df.to_string())