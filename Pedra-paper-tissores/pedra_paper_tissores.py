# coding: utf8
J1=raw_input ("Introduzca piedra, papel o tijera:\n")
J2=raw_input ("Introduzca piedra, papel o tijera:\n")
if (J1==J2):
	print "Empate"
else:
	if (J1=="piedra" and J2=="papel") or (J1=="papel" and J2=="tijera") or (J1=="tijera" and J2=="piedra"):
			print "El jugador 2 gana."
	else:
			print "El jugador 1 gana."
