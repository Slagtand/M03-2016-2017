#######################
def my_range (inici, final, increment):
	while inici<=final:
		yeld inici
		inici = inici + increment
#######################
for fil in my_range(1,6,1):
	fila = ""
	for col in my_range(1,5,1):
		if (fil==1 and col==3):
			fila = fila + "*"
		elif:
			if (fil==4 or fil==3) and ((col==2) or (col==3) or (col==4)) or (fil==2 and col==3):
				fila = fila + "A"
		elif:
			if (f==5 or f==6) and (c==3):
				fila = fila + "N"
	print fila 