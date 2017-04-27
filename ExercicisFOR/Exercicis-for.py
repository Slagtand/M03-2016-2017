# coding: utf8

#Bucle-informes
'''anyo = 2010

# Des de 2010 fins a 2016
for anyo in xrange(anyo,2017):
	print "Informe any", anyo
'''
#Bucles-contar
'''num = 1
for num in xrange (num, 51):
	print num
'''
#Bucles contar2
'''num=1
limite=input("Introduzca un número:\n")
for num in xrange (num, limite+1):
	print num
'''
#Bucle contar pares
'''num=1
limite=input ("Introduzca un número:\n")
for num in xrange (num, limite+1):
	if (num%2==0):
		print num
'''
#Bucle sumar
'''num=1
limite=5
total=0
for num in xrange (num, limite+1):
	total=total+num
	print num, total
'''
#Bucle sumar pares
num=1
limite=10
total=0
for num in xrange (num, limite+1, 1):
	if (num%2==0):
		total=total+num
		print num, total
