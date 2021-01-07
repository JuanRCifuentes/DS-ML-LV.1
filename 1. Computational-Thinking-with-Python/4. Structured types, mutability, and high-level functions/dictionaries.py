my_dictionary = {
    'David': 35,
    'Erika': 32,
    'Jaime': 50
}

print(my_dictionary['David'])

print(my_dictionary.get('Juan', 'Juan not found')) #Looks for Juan, and if that key doesn't exist, returns 'Juan not found'
print(my_dictionary.get('Jaime', 30))

#Reassign
my_dictionary['Jaime'] = 20
print(my_dictionary)

#New value
my_dictionary['Pedro'] = 50
print(my_dictionary)

#Delete
del my_dictionary['Jaime']
print(my_dictionary)

#Iterate
#   Keys
for llave in my_dictionary.keys():
    print(llave)

#   Values
for valor in my_dictionary.values():
    print(valor)

#   Items
for llave, valor in my_dictionary.items():
    print(llave, valor)

#A key exists ?
print('Tom' in my_dictionary)