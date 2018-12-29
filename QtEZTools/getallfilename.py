import os

file_dir = os.getcwd()
for root, dirs, files in os.walk(file_dir):  
    for file in files:
        print(file) #当前路径下所有非目录子文件  
