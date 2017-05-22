# coding= utf8

#Creem el diccionari
diccionari={'M':'Mononoke','C':'Chihiro','N':'Nausicaa'}

#Fem un print del diccionari
print diccionari

#Fem un print sol del valor que tingui M, en aquest cas Mononoke
print(diccionari.get('M'))

#Fem un print sol del valor que tingui N i l'esborrem del diccionari
print(diccionari.pop('N'))

print diccionari

#Fem un print de la key K, ens torna fals perque no existeix al diccionari
print("K" in diccionari)
