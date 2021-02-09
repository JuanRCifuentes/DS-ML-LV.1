my_list = [1, 2, 3]
print(my_list[0])

print(my_list[1:])

#Append
my_list.append(4)
print(my_list)

#Modify
my_list[0] = 'a'
print(my_list)

#Pop
print(my_list.pop()) #Returns the last object in list and also deletes it from the list
print(my_list)

a = [1, 2, 3]
b = a

print(id(a), a, id(b), b) #It points to the same object in memory

c = [a, b]
a.append(5) #Modified a (or the object at whict a is pointing), so it also modified b

print(c)

# Clone a list
d = list(a)
print(d is a)

e = a[:]
print(e is a)

# List comprehension
#   Operations
my_list = list(range(100))

double =  [i * 2 for i in my_list]
print(f'Numbers multiplied by 2: \n {double}')

#   Conditions
even = [i for i in my_list if i%2 == 0]
print(f'Even numbers: \n {even}')

# Python documentation https://docs.python.org/3/tutorial/datastructures.html
