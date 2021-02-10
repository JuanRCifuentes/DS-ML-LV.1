import random

def linear_search(list, goal):
    match = False
    iterations = 0

    for element in list:
        iterations += 1
        if element == goal:
            match = True
            break
    
    return (match, iterations)

if __name__ == '__main__':
    list_size = int(input('List size: '))
    list = [random.randint(0, 100) for i in range(list_size)]
    print(list)

    goal = int(input('Which number do you want to find?: '))

    (found, iter_lin) = linear_search(list, goal)
    print(f'It took {iter_lin} iterations')
    print(f'The goal element {goal} {"is" if found else "is not"} in the list')