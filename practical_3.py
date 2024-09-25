#Find file in the given directory

import os 

dir_name = input("Enter Dir name: ")

first_letter = input("Give first later of file: ")

files = os.listdir(dir_name)

file_lst = []
for i in files:
    if(first_letter == i[0]):
        file_lst.append(i)
    
if(len(file_lst)==0):
    print("File not found")
else:
    for i in file_lst:
        print(i)
