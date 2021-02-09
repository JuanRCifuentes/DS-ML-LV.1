def factorial(n):
    """Calculate the factorial of a number

        n int > 0
        returns n!
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)

n = int(input('Write an integer: '))
print(f'The factorial of {n} is {factorial(n)}')

def fibonacci(n):
    """
    Calculate fibonacci's n'th number

    n int >= 0 (Recursion limit is usually 1000)
    return the fibonacci's n'th number
    """
    if n == 1 or n == 0:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

n_2 = int(input('Write an integer for the fibonacci number: '))
print(fibonacci(n_2))