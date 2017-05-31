# !/usr/bin/python
# coding: utf-8
import os, time

path_to_explore="./Documents/"

for ruta, directorios, archivos in os.walk(path_to_explore):
	for nombre in archivos:
		ruta_completa=os.path.join(ruta, nombre)
		print (ruta_completa)
		ultim_acces=time.ctime (os.path.getatime(ruta_completa))
		print ultim_acces

timedelta=ultim_acces
data_comparar=ultim_acces-timedelta(days=365)

if (data_comparar>=1):
	print "Els següents arxius no s'hi han accedit des de fa més d'1 any:\n", ruta_completa, ultim_acces
