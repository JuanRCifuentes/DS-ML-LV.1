myList1 = [True, True, True]
myList2 = [True, True, False]
myList3 = [False, False, False]

# ALL - Returns true if every element of the iterable is True
print('----- all()')
print(all(myList1))
print(all(myList2))
print(all(myList3))

# ANY - Returns true if at least one element of the iterable is true
print('----- any()')
print(any(myList1))
print(any(myList2))
print(any(myList3))