#############
def my_range(inici, fi, increment):
	while inici <= fi:
		yield inici
		inici = inici + increment
		
###################
for fil in my_range(1,5,1):
	for col in my_range (1,4,1):
		if (fil==1):
			if (col==1):
				print "-"
			if (col==2):
				print "A"
			if (col==3):
				print "B"
			if (col==4):
				print "C"
		if (col==1):
			if (fil==2):
				print 1
			if (fil==3):
				print 2
			if (fil==4):
				print 3
			if (fil==5):
				print 4
		else:
			print "-"
