listaprueba=["Maria", 8,"Antonio"]

print (listaprueba[:])

listaprueba.append(True)

print (listaprueba[:])

listaprueba.insert(1,"jorge")

print (listaprueba[:])

listaprueba.extend(["camlina",6.8,"ana","lucia"])

print (listaprueba[:])

print(listaprueba.index("camlina"))

print ("Antonio2" in listaprueba)

listaprueba.remove("jorge")
print (listaprueba[1])

listaprueba.pop()

print(listaprueba[:])