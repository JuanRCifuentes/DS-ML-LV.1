#With keys
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict1_keys = [k for k in dict1.keys()]
print(dict1_keys)

#With values
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict1_values = [k for k in dict1.values()]
print(dict1_values)

#With items
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict1_items = {llaves:valores for (llaves, valores) in dict1.items()}
print(dict1_items)

#Now we deal with a condition
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict1_items = {llave:valor for (llave, valor) in dict1.items() if valor > 2}
print(dict1_items)

#Testing...
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict1_keysfun = {k:k*2 for k in dict1.keys()}
print(dict1_keysfun)