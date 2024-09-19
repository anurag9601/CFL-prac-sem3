# import os
# import fnmatch

# def list_files_by_prefix(directory, prefix):
#     try:
#         if not os.path.isdir(directory):
#             print(f"Either the directory '{directory}' does not exist or is not valid.")
#             return
#         matching_files = fnmatch.filter(os.listdir(directory), f"{prefix}*")

#         if not matching_files:
#             print(f"No files starting with '{prefix}' were found in '{directory}'.")
#         else:
#             print(f"Files starting with '{prefix}' in '{directory}':")
#             for filename in matching_files:
#                 print(filename)
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     directory = input("Enter Directory: ")
#     prefix = input("Enter first letter (or prefix) of file: ")

#     list_files_by_prefix(directory, prefix)

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