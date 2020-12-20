# ----- While -----
index = 0
while index < 10:
    print(index)
    index += 1
    if index == 5:
        break

# ----- For -----
frutas = ['manzana', 'banano', 'naranja']
for fruta in frutas:
    print(fruta)

# Using Dictionaries
estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4
}
for pais in estudiantes:
    print(pais)
for pais in estudiantes.keys():
    print(pais)
for numeros in estudiantes.values():
    print(numeros)
for items in estudiantes.items():
    print(items)

# ----- iter() -----
colores = ['azul', 'amarillo', 'rojo']
iterador = iter(colores)
print(next(iterador))
print(next(iterador))
print(next(iterador))