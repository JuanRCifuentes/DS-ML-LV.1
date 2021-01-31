import time
import sys
import resource

print (resource.getrlimit(resource.RLIMIT_STACK))

# resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(1000000)

def timer(funct):
    def wrapper_function(*Args, **Kwargs):
        time0 = time.time()
        answer = funct(*Args, **Kwargs)
        print(f'La función {funct.__name__} demoró {time.time() - time0} en correr')
        return answer
    return wrapper_function

@timer
def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n - 1)

n = 200000

print(sys.getrecursionlimit())

factorial(n)

# time0 = time.time()
# factorial_r(n)
# print(f'La función factorial_r demoró {time.time() - time0} en correr')
