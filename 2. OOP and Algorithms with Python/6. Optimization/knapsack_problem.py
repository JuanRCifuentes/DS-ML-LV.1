def my_knapsack_attempt(things, max_capacity):
    items = dict_to_list(things)

    for i in items:
        price = i[1][0]
        weight = i[1][1]
        i.append(weight/price)
    # print(items)

    items = bubble_sort(items)
    # print(items)

    # Adding items to bag, first the ones with lowest weight/price factor
    bag = []
    item_i = 0
    capacity = max_capacity
    while capacity>0 and item_i<len(items):
        item = items[item_i]

        if(capacity - item[1][1] >= 0):
            bag.append(item)
            capacity -= item[1][1]
            item_i += 1
        else:
            item_i += 1

    return bag

def dict_to_list(dict):
    items = []

    for key, value in dict.items():
        temp = [key,value]
        items.append(temp)
    
    return(items)

def bubble_sort(list):
    n = len(list)

    for i in range(n):
        for j in range(0, n - i - 1):

            if list[j][2] < list[j+1][2]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def backpack(size, weights, values, n):
    print(size)
    if n==0 or size==0:
        return 0
    
    if weights[n-1]>size:
        return backpack(size, weights, values, n-1)
    
    return max( values[n-1] + backpack( size-weights[n-1], weights, values, n-1 ),
                backpack(size, weights, values, n-1))

if __name__ == "__main__":
    values = [60, 100, 120, 10]
    weights = [10, 20, 30, 10]
    bag_size = 60
    n = len(values)

    resultado = backpack(bag_size, weights, values, n)
    print(resultado)

    # Eash thing has a price ($) and weight (kg)
    things = {
    'green': (4, 12),
    'blue': (2, 2),
    'grey': (2, 1),
    'red': (1, 1),
    'yellow': (10, 4)
    }

    # Capacity in kg
    capacity = 15

    print(my_knapsack_attempt(things, capacity))