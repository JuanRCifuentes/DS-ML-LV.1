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

#Interesting Comprehension applications

#-----Replacing certain loops-----
numbers = range(10)

# Loop version
new_dict_for = {}
for n in numbers:
    if n%2==0:
        new_dict_for[n] = n**2

print(new_dict_for)

#Comprehension version
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

print(new_dict_for)

#-----Replacing functions-----
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

# Function version
def fahrenheit_to_celsius(temperature):
    return (float(5)/9)*(temperature-32)

celsius = []
for i in fahrenheit.values():
    celsius.append(fahrenheit_to_celsius(i))

celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)

# Lambda function version
    #Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

    #Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)

# Comprehension version
    #Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

print(celsius_dict)
