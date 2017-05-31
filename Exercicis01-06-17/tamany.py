# coding:utf-8
import os
#Indiquem la ruta que volem explorar 
path_to_explore="./Documents/"
total_size=0
        
# Mostrem ruta tot    
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        name_path=os.path.join(root, name)
	#Mostrem el tamany de cada arxiu
        tamany=os.stat(name_path).st_size
        
#Comparem si l'arxiu és supeior o igual a 1 GB (2³⁰ B son 1 GB)
if (tamany>=2**30):
	print "Els arxius que ocupen més d'1GB són:\n", name_path , tamany
