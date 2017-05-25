# !/usr/bin/python
# coding:utf-8
import os
import stat

path_to_explore="./Documents/"

#####################################################################
# Mostrem ruta tot
def comprobacio_perm (path_to_explore):
    for root, dirs, files in os.walk(path_to_explore):
        for name in files:
            name_path=os.path.join(root, name)
            print(name_path) ,
            permissions = oct(stat.S_IMODE ( os.stat (name_path).st_mode ))
            return permissions


        for name in dirs:
            name_path=os.path.join(root, name)
            print(name_path) ,
            permissions = oct(stat.S_IMODE ( os.stat (name_path).st_mode ))
            return permissions


############################################################
if (comprobacio_perm[-1]!= 0):
    print name_path
    print "Atenció!"
else:
    "No té errors de seguretat"
