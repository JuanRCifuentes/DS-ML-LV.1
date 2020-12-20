import datetime

goal = int(input('Choose an integer: '))
time_0 = datetime.datetime.now()

epsilon = 0.01
paso = epsilon**2
answer = 0.0

while abs(answer**2 - goal) >= epsilon and answer <= goal:
    #print(abs(answer**2 - goal), answer)
    answer += paso

time_1 = datetime.datetime.now()

tot_time = (time_1 - time_0).microseconds / 1000

if abs(answer**2 - goal) >= epsilon:
    print(f'Square root of {goal} not found (Answer in {tot_time} miliseconds)')
else:
    print(f"The square root of {goal} is {answer} (Answer in {tot_time} miliseconds)")

