import linear_search
import binary_search
import random

if __name__ == '__main__':
    list_size = int(input('List size: '))
    list = sorted([random.randint(0, 100) for i in range(list_size)])
    # print(list)

    goal = int(input('Which number do you want to find?: '))

    print('-----')
    print('LINEAR SEARCH:')
    (found, iter_lin) = linear_search.linear_search(list, goal)
    print(f'It took {iter_lin} iterations')
    print(f'The goal element {goal} {"is" if found else "is not"} in the list')

    print('-----')
    print('BINARY SEARCH:')
    (found, iter_bin) = binary_search.binary_search(list, 0, len(list)-1, goal)
    print(f'It took {iter_bin} iterations')
    print(f'The goal element {goal} {"is" if found else "is not"} in the list')