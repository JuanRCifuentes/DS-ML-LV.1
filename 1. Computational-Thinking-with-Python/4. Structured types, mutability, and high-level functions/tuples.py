tuple_name = ('Hello', 'World', 55)
list_name = ['Hello', 'World', 55]

my_tuple = ()
print(type(my_tuple))

# Reassign variable, not modify the tuple
my_tuple = (1, 'dos', True)
print(my_tuple[1])

# Modify a tuple will lead to an error
# my_tuple[0] = 5

# To declare a tuple with a sigle element we just gotta put a comma
not_a_tuple = (1)
print(type(not_a_tuple))

number_tuple = (1,)
float_tuple = (1.5,)
string_tuple = ('Hello World!',)
print(type(string_tuple), type(float_tuple), type(number_tuple))

my_other_tuple = (2, 3, 4)
my_tuple += my_other_tuple #Reassigned my_tuple value

print(my_tuple)

# Assign tuple values to variables
x, y, z = my_other_tuple
print(x, y, z)

# Function returning tuple
def coordenadas():
    return (5, 4)

coordenada = coordenadas()
x, y = coordenadas()

print(coordenada, x, y)