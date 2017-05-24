# !/usr/bin/python
# coding:utf-8

import os

#Canviem els permisos del fitxer
path1="/home/mint/Documents/exercici_walk.py"

os.chmod(path1, 700)

##################################################

#Canviem els permisos de la carpeta
path2="/home/mint/Documents/exercici1"

os.chmod(path2, 777)

###################################################

#Llistem els arxius i directoris de
for root, dirs, files in os.walk("." , topdown=True):
	for name in files:
		print (os.path.join(root, name))
	for name in dirs:
		print (os.path.join(root, name))
