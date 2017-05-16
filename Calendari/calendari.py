#coding:utf-8

#Fem un import del calendari
import calendar

#Establim quin mes de quin any vol l'usuari i establim el contador
mes = input ("Introduzca el mes (1-12):\n ") 
any = input ("Introduzca el año (AAAA):\n ")
num=1

#Fem servir les funcions de monthrange (rang dels mesos) i weekday (dia de la setmana)
num_dias_mes = calendar.monthrange(any, mes)[1]
dia_semana = calendar.weekday(any, mes, 1)

#Creem la variable de dies màxims que pot tindre cada mes
dias_max = num_dias_mes

#Definim el my_range
#######################################################
def my_range(inici, fi, increment):
    while inici <= fi:
        yield inici
        inici = inici + increment
#######################################################

#Printem la capçalera
print "| L | M | X | J | V | S | D |"
print "|---------------------------|"

#Per a la primera línia, dibuixem el dia de setmana que comença el mes, els anteriors estàn en blanc.
for fil in my_range (1, 1, 1):
	for col in my_range (1, dia_semana -1 ,1):
		print " ",
	for col in my_range (dia_semana, 7, 1):
		print num,
		num = num + 1
	print " "

#Per a les línies següents, dibuixem la resta dels dies fins que és igual o menor al màxim.
for fil in my_range (1,5,1):
	for col in my_range (1,7,1):
		if num <= dias_max:
			print num,
			num = num + 1
		else:
			print " ",
	
	print " "
