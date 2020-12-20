import datetime

chosen_method = int(input('Choose a method' + \
    'to get the square root (1. Binary Search, 2. Aproximation, 3. Enumeration): '))

def binary_method():
    goal = int(input('Choose an integer: '))
    time_0 = datetime.datetime.now()

    epsilon = 0.001
    low = 0.0
    high = max(1.0, goal)
    answer = (high + low) / 2

    while abs(answer**2 - goal) >= epsilon:
        if answer**2 < goal:
            low = answer
        else:
            high = answer

        answer = (high + low) / 2
        print(answer)

    time_1 = datetime.datetime.now()

    tot_time = (time_1 - time_0).microseconds / 1000

    print(f"The square root of {goal} is {answer} (calculated in {tot_time} miliseconds)")

def enum_method():
    goal = int(input("Choose an integer: "))
    time_0 = datetime.datetime.now()

    answer = 0

    while answer**2 < goal:
        answer += 1

    time_1 = datetime.datetime.now()
    tot_time = (time_1 - time_0).microseconds / 1000

    if answer**2 == goal:
        print(f"The squere root of {goal} is {answer} (Answer in {tot_time} miliseconds)")
    else:
        print(f"{goal} doesn't have an exact square root (Answer in {tot_time} miliseconds)")

def aprox_method():

    goal = int(input('Choose an integer: '))
    time_0 = datetime.datetime.now()

    epsilon = 0.001
    paso = epsilon**2
    answer = 0.0

    while abs(answer**2 - goal) >= epsilon and answer <= goal:
        print(abs(answer**2 - goal), answer)
        answer += paso

    time_1 = datetime.datetime.now()
    tot_time = (time_1 - time_0).microseconds / 1000

    if abs(answer**2 - goal) >= epsilon:
        print(f'Square root of {goal} not found (Answer in {tot_time} miliseconds)')
    else:
        print(f"The square root of {goal} is {answer} (Answer in {tot_time} miliseconds)")

if chosen_method == 1:
    binary_method()
elif chosen_method == 2:
    aprox_method()
elif chosen_method == 3:
    enum_method()
else:
    print('You must write a number between 1 and 3.')
    