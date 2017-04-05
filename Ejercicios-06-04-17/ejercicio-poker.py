# coding: utf8

from random import randint 
random1=randint(1,4)
random2=randint(1,4)
num1=randint(1,13)
num2=randint(1,13)

# Banca
if (random1==1):
	classe1="Picas"
if (random1==2):
	classe1="Diamantes"
if (random1==3):
	classe1="Tréboles"
if (random1==4):
	classe1="Corazones"
if (num1<=10):
	carta1=num1
if (num1==11):
	carta1="J"
if (num1==12):
	carta1="Q"
if (num1==13):
	carta1="K"

# Jugador
if (random2==1):
	classe2="Picas"
if (random2==2):
	classe2="Diamantes"
if (random2==3):
	classe2="Tréboles"
if (random2==4):
	classe2="Corazones"
if (num2<=10):
	carta2=num2
if (num2==11):
	carta2="J"
if (num2==12):
	carta2="Q"
if (num2==13):
	carta2="K"

# Resultado
print "La banca tiene", carta1, classe1
print "El jugador tiene", carta2, classe2

if (num1>num2):
	print "La banca gana."
else:
	print "El jugador gana."
