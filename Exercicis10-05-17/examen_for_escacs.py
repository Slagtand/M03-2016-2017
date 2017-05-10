#######################
def my_range (inici, final, increment):
	while inici<=final:
		yeld inici
		inici = inici + increment
#######################
for fil in my_range(1,8,1):
	for col in my_range(1,8,1):
		if (fil%2==0):
			if (col%2==0):
				print "B"
			else:
				print "W"
		else:
			if (col%2==0):
				print "W"
			else:
				print "B"
	print " "