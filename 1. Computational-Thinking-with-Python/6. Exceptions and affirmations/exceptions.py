def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

list_1 = list(range(10))
number = 0

print(divide_elementos_de_lista(list_1, number))