print ("How many slices you have in your pizza?")
StartPizza = int (input (""))
print ("How many you eat?")
SlicesEated = int (input (""))
def PizzasRestantes():
    TotalPizza = StartPizza - SlicesEated
    return TotalPizza

PizzasRestantes