# coding: utf8

from random import randint

J1=raw_input ("Introduzca piedra, papel, tijera, lagarto o spock:\n")
J2= randint (1,5)

if (J2==1):
	J2 = "PI"
if (J2==2):
	J2 = "PA"
if (J2==3):
	J2 = "TI"
if (J2==4):
	J2 = "LA"
if (J2==5):
	J2 = "SP"
print "La máquina elige", J2

if (J1==J2):
	print "Empate"
else:
	if (J1=="PI") and ((J2=="LA") or (J2=="TI")):
		print "Jugador 1 gana"
	else:
		print "Jugador 2 gana"
	if (J1=="PA") and ((J2=="PI") or (J2=="SP")):
		print "Jugador 1 gana"
	else:
		print "Jugador 2 gana"
	if (J1=="TI") and ((J2=="PA") or (J2=="LA")):
		print "Jugador 1 gana"
	else:
		print "Jugador 2 gana"
	if (J1=="LA") and ((J2=="PA") or (J2=="SP")):
		print "Jugador 1 gana"
	else:
		print "Jugador 2 gana"
	if (J1=="SP") and ((J2=="PI") or (J2=="TI")):
		print "Jugador 1 gana"
	else:
		print "Jugador 2 gana"