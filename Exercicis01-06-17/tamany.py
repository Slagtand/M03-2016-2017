# coding:utf-8
import os
 
path_to_explore="./Documents/"
total_size=0
        
# Mostrem ruta tot    
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        name_path=os.path.join(root, name)
        tamany=os.stat(name_path).st_size
        

if (tamany>=2**30):
	print "Els arxius que ocupen més d'1GB són:\n", name_path , tamany
