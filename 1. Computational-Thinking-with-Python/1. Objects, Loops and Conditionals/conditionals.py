name_1 = input("Nombre del primer sujeto ")
name_2 = input("Nombre del segundo sujeto ")
age_1 = int(input("Edad de "+ name_1 + " "))
age_2 = int(input("Edad de "+ name_2 + " "))


if age_1 > age_2:
    print(name_1 + " es más viejo que " + name_2 )
elif age_1 < age_2:
    print(name_2 + " es más viejo que" + name_1 )
else:
    print('Ambos tienen la misma edad')
