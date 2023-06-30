import os
import sys
import urllib

#Lists files in given directory (such as from drag and drop). Otherwise lists files in current directory.

directory_path = os.getcwd()

if len(sys.argv) > 1:
	directory_path = str(sys.argv[1])
	
files_list = os.listdir(directory_path)

with open('files_list.txt', 'w',encoding='utf8') as f:

	for file in files_list:
		f.write(file)
		f.write('\n')