X = True

car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}
while (X!=False):
    informacion_requerida=input("Escribe la información que queires revisar: ")
    informacion_requerida_organizada= informacion_requerida.lower()
    print(car[informacion_requerida_organizada])
    print ("¿Quieres revisar otra información?", "[S/N]") 
    opción=input("-")
    if opción=="S":
    	X = True
    else: 
    	X = False 