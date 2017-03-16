# coding: utf8

print "Menú de calculadora:\n"
print "Qué desea hacer el amo?\n"
print "S) Salir\n"
print "1) Sumar\n"
print "2) Restar\n"
print "3) Multiplicar\n"
print "4) Dividir\n"

opcio = raw_input("Introduzca la opción:\n")
if (opcio=="S" or opcio=="s"):
	print "Opción salir"
if (opcio=="1"):
	print "Opción sumar"
if (opcio=="2"):
	print "Opción resta"
if (opcio=="3"):
	print "Opción multiplicar"
if (opcio=="4"):
	print "Opción división"
if (opcio>="1" and opcio<="4") or (opcio=="s" or opcio=="S"):
	print " "
else:
	print "Esta opción no existe"
