import pandas as pd 


def replacing(df, column):
    n = int(input("how many characters do you want to delete or replace : ",))
    inputs = []
    for i in range(n):
        value =  input('enter the character :',)
        inputs.append(value)    
    choice = input("do you want to replace these characters or delete them (delete/replace) :",)
    if choice == 'delete':
        for char in inputs:
            df[column] = df[column].str.replace(char, '', regex=True)
    elif choice == 'replace':
        replace = input('replaced by what ? :',)
        for char in inputs:
            df[column] = df[column].str.replace(char, replace, regex=True)
    else:
        print('error')

    return df
    
   

file_name = input("enter the file name that u want to clean : ", )
df = pd.read_csv(file_name)
print(df.to_string())


print('starting by deleting duplicates raws')
df = df.drop_duplicates()


column = df.shape[1]
for x in range(column):
    column = df.columns[x]
    answer = input('do you want to clean the column named :' +column +'(Yes/No)')
    
    if answer == 'YES' or 'yes':
        answer = input('do you want to delete an entire raw because of empty cells (Yes/No)')
        if answer == 'YES' or 'yes':
            df = df.dropna(subset=[column])
        elif answer == 'NO' or 'no':
            pass


        answer = input('do you want to replace or delete some characters (Yes/No)')
        if answer == 'YES' or 'yes':
            df = replacing(df, column)
        elif answer == 'NO' or 'no':
            pass    




    elif answer == 'NO' or 'no':
        pass    



