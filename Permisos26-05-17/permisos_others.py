# !/usr/bin/python
# coding:utf-8
import os
import stat

path_to_explore="./Documents/"
permissions1=0
permissions2=0

#####################################################################
# Mostrem ruta tot
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        name_path=os.path.join(root, name)
        permissions1 = oct(stat.S_IMODE ( os.stat (name_path).st_mode ))
    for name in dirs:
        name_path=os.path.join(root, name)
        permissions2 = oct(stat.S_IMODE ( os.stat (name_path).st_mode ))



############################################################
if ((permissions1[-1]!= 0) or (permissions2[-1]!= 0)):
    print name_path
    print "Atenció!"
else:
    "No té errors de seguretat"
