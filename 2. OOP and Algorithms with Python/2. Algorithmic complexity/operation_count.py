import time

def timer(funct):
    def wrapper_function(*Args, **Kwargs):
        time0 = time.time()
        answer = funct(*Args, **Kwargs)
        print(f'La función {funct.__name__} con parámetros {Args[0]} demoró {time.time() - time0} en correr')
        return answer
    return wrapper_function

@timer
def f(x):
    respuesta = 0

    for i in range(1000):
        respuesta += 1

    for i in range(x):
        respuesta += 1

    for i in range(x):
        for j in range(x):
            respuesta += 1  
            respuesta += 1

    return respuesta

print(f(5))
print(f(1000))
print(f(10000))
# print(f(100000)) #Ya estaba tardando más de 10 minutos
# print(f(1000000)) #Habría tardado casi un día, extrapolando el tiempo que tomó con 10k
