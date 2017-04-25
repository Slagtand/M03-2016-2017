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
#Definicio de my_range
########################################
def my_range(num, limit, increment):
	while num <= limit:
		yield num
		num= num + increment
		if (num%2==0):
			total=total+num
#########################################		
num=1
limit=10
total=0
for num in my_range(num, limit, 2):
	print num, total 
