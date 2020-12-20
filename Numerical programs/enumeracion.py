#Getting the square root of an integer trying every number from zero
goal = int(input("Choose an integer: "))
answer = 0

while answer**2 < goal:
    answer += 1

if answer**2 == goal:
    print(f"The squere root of {goal} is {answer}")
else:
    print(f"{goal} doesn't have an exact square root")

    