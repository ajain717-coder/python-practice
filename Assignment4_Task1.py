import os
file_name=("sample.txt")
if os.path.exists(file_name):
    file=open(file_name,"r")
    line1=file.readline()
    line2=file.readline()
    print("Reading file content:")
    print(f"Line 1: {line1}")
    print(f"Line 2: {line2}")
else:
    print(f"Error:The file {file_name} was not found")

file.close()