# Functions as arguments for other functions
def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    return resultados

nums = [1, 2, 3]
print(aplicar_operacion(multiplicar_por_dos, nums))

print(aplicar_operacion(sumar_dos, nums))

# Use "lambda" to define a function as an expression
sumar = lambda x, y: x + y

print(sumar(5, 3))

# Functions in data structures
print(abs(2))
def aplicar_operaciones(num):
    operaciones = [abs, float] #Here, the functions are inside a list

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

print(aplicar_operaciones(-2))