from varname import nameof

def decorator_function(funct):
    def wrapper():
        print('This is the last message')
        funct()
        print('This is the first message')
    return wrapper

def buzz1():
    print('Buzzz')

buzz = decorator_function(buzz1)

buzz()

#-----With better sintaxis-----
def decorator_function2(funct):
    def wrapper():
        print('This is the last message')
        funct()
        print('This is the first message')
    return wrapper

@decorator_function2
def buzz2():
    print('Buzzz')

buzz()

#-----Understanding decorators-----
def deco(funct):
    print(f'Ejecutando el método {deco.__name__} con id {id(deco)}')
    print(f'El ID de la función parámetro {funct.__name__} es: {id(funct)}')
    def wrapper_func(x):
        print(f'Ejecutando wrapper con la función {funct.__name__} (id:{id(funct)}) como parámetro')
        funct(x)

    print(f'El ID de la función {wrapper_func.__name__} es: {id(wrapper_func)}')
    return wrapper_func

#@deco
def original_1(msg):
    print(f'Ejecutando la función {original_1.__name__} con {msg}')

variable_juan = original_1

print(f'El ID de la función {original_1.__name__} es: {id(original_1)}')

original_1 = deco(original_1)

print(f'El ID de la variable {nameof(original_1)} es: {id(original_1)}')

variable_juan.__name__ = 'test'

#@deco
def original_2(msg):
    print(f'Ejecutando la función {original_2.__name__} con {msg}')

print(f'El ID de la función {original_2.__name__} es: {id(original_2)}')

original_2 = deco(original_2)

print(f'El ID de la variable {nameof(original_2)} es: {id(original_2)}')

original_1('MESSAGE')
original_2('MESSAGE')
