# coding: utf8

sortir=False
sortir_apuesta=False
saldo=100

print "Tu saldo es:", saldo 

apuesta=input("Introduzca su apuesta:\n")
while sortir_apuesta==False:
	if (apuesta==-1):
		sortir_apuesta=True
		sortir=True
	else:
		if (apuesta>=10 and apuesta<=saldo):
			sortir_apuesta=True
		else:
			print "Su apuesta no es válida, debe de ser 10 mínimo y no superar su saldo"
			apuesta=input("Introduzca su apuesta:\n")
