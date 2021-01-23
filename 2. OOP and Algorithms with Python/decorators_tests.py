import time

def timer(funct):
    def wrapper_function(*Args, **Kwargs):
        time0 = time.time()
        funct(*Args, **Kwargs)
        print(f'La función {funct.__name__} demoró {time.time() - time0} en correr')
    return wrapper_function

class Decorador_Class(object):
    
    def __init__(self, function_1):
        self.function_1 = function_1
    
    def __call__(self, *Args, **Kwargs):
        print(f'Ejecutando mi clase decoradora con la funcion {self.function_1.__name__} {Args[0]}')
        self.function_1(*Args, **Kwargs)

# @timer
@Decorador_Class
def buzz1(mensaje):
    print(mensaje)

# buzz1 = Decorador_Class(buzz1)
# buzz1 = timer(buzz1)

@timer
def buzz2():
    print('Buzzz_A')

buzz1('H')
buzz2()
buzz1('Hola')
buzz2()
buzz1('Hello')
buzz2()
buzz2()