def factorial(n: int):
    """Calculate the factorial of a number

        Parameters:
        - n: int
            n > 0 (Recursion limit is usually 1000)

        Returns: n! = Result of the mathematical factorial operation over n.
    """
    
    if n == 1:
        return 1

    return n * factorial(n - 1)

def fibonacci(n: int):
    """
    Calculate fibonacci's n'th number

    - n int >= 0 (Recursion limit is usually 1000)

    - returns the fibonacci's n'th number
    """

    if n == 1 or n == 0:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input('Write an integer: '))
    print(f'The factorial of {n} is {factorial(n)}')

    n_2 = int(input('Write an integer for the fibonacci number: '))
    print(fibonacci(n_2))
    factorial()

if __name__ == '__main__':
    main()
