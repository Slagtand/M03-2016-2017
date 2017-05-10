#######################
def my_range (inici, final, increment):
	while inici<=final:
		yeld inici
		inici = inici + increment
#######################
for fil in my_range(1,4,1):
	for col in my_range(1,8,1):
		if (fil==1):
			print "x",
		elif (fil==4):
			print "x",
		else:
			if (col==1):
				print "x",
			elif (col==8):
				print "x"
			else:
				if (fil==2):
					if (col==4) or (fil==5):
						print "·"
				elif (fil==3):
					if (col==4):
						print "\\",
					elif (col==5):
						print "/"
	print " "