import random

def binary_search(list, start, end, goal, iter_bin=0):
    iter_bin += 1
    # print(iterations)
    # print(start, end)
    
    middle = (start + end) // 2

    if start > end:
        return (False, iter_bin)
    elif list[middle] == goal:
        return (True, iter_bin)
    elif list[middle] < goal:
        return binary_search(list, middle+1, end, goal, iter_bin)
    else:
        return binary_search(list, 0, middle-1, goal, iter_bin)

if __name__ == '__main__':
    list_size = int(input('List size: '))
    list = sorted([random.randint(0, 100) for i in range(list_size)])
    print(list)

    goal = int(input('Which number do you want to find?: '))
    
    (found, iter_bin) = binary_search(list, 0, len(list)-1, goal)
    print(f'It took {iter_bin} iterations')
    print(f'The goal element {goal} {"is" if found else "is not"} in the list')