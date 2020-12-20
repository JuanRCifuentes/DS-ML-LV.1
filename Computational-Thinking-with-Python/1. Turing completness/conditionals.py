name1 = input("Nombre del primer sujeto ")
name2 = input("Nombre del segundo sujeto ")
edad_1 = int(input("Edad de "+ name1+ " "))
edad_2 = int(input("Edad de "+ name2+ " "))


if edad_1 > edad_2:
    print(name1 + " es más viejo que " + name2 )
elif edad_1 < edad_2:
    print(name2 + " es más viejo que" + name1 )
else:
    print('Ambos tienen la misma edad')
