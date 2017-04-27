#Bucle sumar pares
#Definicio de my_range
########################################
def my_range(num, limit, increment):
	while num <= limit:
		yield num
		num= num + increment
		if (num%2==0):
			total=total+num
#########################################		
num=1
limit=10
total=0
for num in my_range(num, limit, 2):
print num, total 
