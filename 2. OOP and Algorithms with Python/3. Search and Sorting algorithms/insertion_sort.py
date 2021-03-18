import list_tester # type: ignore

def insertion_sort(list):

    #Steps through every place on the list except the first one
    for i in range(1, len(list)):
        current_value = list[i] #The number we are placing in the correct spot
        current_position = i # Always starts next to the sorted sublist

        #Steps through the list to the first position, comparing with every sorted number. Stops when comparing with an equal or smaller number
        while current_position > 0 and current_value < list[current_position-1]: 
            list[current_position] = list[current_position-1]
            current_position -= 1

        list[current_position] = current_value

    return list

if __name__ == '__main__':
    list_tester.test_method(insertion_sort)