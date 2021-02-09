my_range = range(1, 5)
print(type(my_range), my_range)

my_range = range(0, 7, 2)
my_range2 = range(0, 8 ,2)

# Value equality
print(my_range == my_range2) # those are the same because the finish number is not included

range1 = id(my_range)
range2 = id(my_range2)

#Oject equality
print(range1==range2, my_range is my_range2) # Not the same oject

print('Even numbers')
for i in range(0, 101, 2):
    print(i)

print('Odd numbers') # Odd numbers are called "nones" in mexican
for i in range(1, 100, 2):
    print(i)
