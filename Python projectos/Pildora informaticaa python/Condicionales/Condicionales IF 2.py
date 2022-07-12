#else = y si no es verdad 
print("VERIFIVACIÓN DE ACCESO")
#int para pasar a entero
edad_usuario=int(input("Introduce tu edad: "))

if edad_usuario<18:
	print("No tienes acceso")
#elif se usa para que el else se acompañe de toda la estructura 
elif edad_usuario>100:
	print("Edad incorrecta")
else:
	print("Puedes pasar")
	print ("Bienvenido")
#no puede haber dos else seguidos, cada else debe tener un if

print("PROGRAMA FINALIZADO")