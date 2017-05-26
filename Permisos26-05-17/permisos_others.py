# !/usr/bin/python
# coding:utf-8
import os
import stat

path_to_explore="./Documents/"
permissions1=0
permissions2=0

#####################################################################
# Fem un for per a que recorri cada carpeta i fitxer recursivament.
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        name_path=os.path.join(root, name)
        # Treiem els permisos
        permissions1 = oct(stat.S_IMODE ( os.stat (name_path).st_mode ))
    for name in dirs:
        name_path=os.path.join(root, name)
        # Treiem els permisos
        permissions2 = oct(stat.S_IMODE ( os.stat (name_path).st_mode ))



############################################################
# Comparem els resultats dels permisos de others amb el [-1], si és diferent a 0 salta la alarma
if ((permissions1[-1]!= 0) or (permissions2[-1]!= 0)):
    print name_path
    print "Atenció!"
else:
    "No té errors de seguretat"
