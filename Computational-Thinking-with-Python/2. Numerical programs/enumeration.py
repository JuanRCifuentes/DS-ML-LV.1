import datetime

#Getting the square root of an integer trying every number from zero
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