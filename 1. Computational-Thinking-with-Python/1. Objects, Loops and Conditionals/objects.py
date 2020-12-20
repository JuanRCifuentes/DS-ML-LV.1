# ----- TYPES -----
w = True
print(type(w))
x = 5
print(type(x))
y = 'Hello World!'
print(type(y))
z = 1.0
print(type(z))

# ----- EXPRESSIONS -----

print(1 + 2)
#print(1 3.0) #-> This is a SyntaxError because there is no operator between objects
#print(5 / 'Platzi') #-> This is a semantic error because a art cannot divide an int
print(5 * 'Platzi')

print('2 - 5 = ' + str(2 - 5))
print('2.0 * 3 = ' + str(2.0 * 3))
print('6 // 2 = ' + str(6 // 2))
print('6 // 4 = ' + str(6 // 4))
print('6 / 4 = ' + str(6 / 4))
print('7 % 2 = ' + str(7 % 2))
print('2**3 = ' + str(2**3))

# ----- STRINGS -----
name = "Felix Kjellberg"

print(name)
print(len(name))
print(name[2])
print(name[:5])
print(name[2:10])
print(name[::2])

string_1 = f'Hola {name * 5}'
string_2 = "Hola " + name * 5
print(string_1)
print(string_2)

# ----- FLOATS -----
x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')