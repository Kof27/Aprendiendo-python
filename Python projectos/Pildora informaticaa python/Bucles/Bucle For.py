for i in ["Samsung","Apple","Xiaomi"]:
	#con el argumento end determinamos como quiere que termine el print, en este caso el End es para que no haya salto de linea
	print (i, end=" ")

email=False
contador=0  
print("Please write your email")
Miemail=input("-")
for i in Miemail:
	if(i=="@" or i=="."):
		email=True
		contador = contador + 1
#si se quita el ==true seguira funcionando igual pues python lo tomara si buscamos que es verdadero
if email==True and contador==2:
	print ("Email correcto")
else:
	print("Email incorrecto")