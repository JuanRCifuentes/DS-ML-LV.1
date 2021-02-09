import datetime

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