# coding : utf8
num = 31
J1=num%7
J2=num%5
sortir=False
while sortir==False:
	print num
	if (J1==0 or J1==1):
		print "Jugador1 = Tissores"
		J1="Tijeras"
	if (J1==2 or J1==3 or J1==6):
		print "Jugador1 = Pedra"
		J1="Piedra"
	if (J1==4 or J1==5):
		print "Jugador1 = Paper"
		J1="Papel"
	if (J2==0 or J2==1 or J2==2):
		print "Jugador2 = Paper"
		J2="Papel"
	if (J2==3):
		print "Jugador2 = Tissores"
		J2="Tijeras"
	if (J2==4):
		print "Jugador2 = Pedra"
		J2="Piedra"
	if (J1==J2):
		print "Empat"
	else:
		if (J1=="Piedra" and J2=="Papel") or (J1=="Papel" and J2=="Tijeras") or (J1=="Tijeras" and J2=="Piedra"):
			print "El jugador 2 gana"
		else:
			print "El jugador 1 gana"
	if (num==57):
		sortir=True
	num = num + 1
