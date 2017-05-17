# coding: utf8

##################################
#Afegim valor a una llista buida
llista_afegir = []
print llista_afegir
llista_afegir.append(9)
llista_afegir.append(8)
llista_afegir.append(95)
llista_afegir.append(5)
print llista_afegir
print llista_afegir[2]
######################################
print "-----------------------------------"
##################################
#Insertem un valor en una llista creada
llista_insertar= [1,55,"Hola",9,7]
print llista_insertar
llista_insertar.insert(3,"Que tal")
print llista_insertar
####################################
print "----------------------------"
##################################
#Eliminem un valor de la llista
llista_esborrar= [1,2,3,4,5,6,"Aixo s'esborra"]
print llista_esborrar
llista_esborrar.remove("Aixo s'esborra")
print llista_esborrar
del llista_esborrar[5]
print llista_esborrar
#################################
print "--------------------------"
