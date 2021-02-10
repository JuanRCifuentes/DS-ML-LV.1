import random

def linear_search(list, goal):
    match = False

    for element in list:
        if element == goal:
            match = True
            break

    return match

if __name__ == '__main__':
    list_size = int(input('List size ?'))
    goal = int(input('Which number do you want to find?'))

    list = [random.randint(0, list_size) for i in range(list_size)]

    sq = "\'" #SyntaxError: f-string expression part cannot include a backslash
    found = linear_search(list, goal)

    print(list)
    print(f'The goal element {goal} {"is" if found else "isn" + sq + "t"} in the list')