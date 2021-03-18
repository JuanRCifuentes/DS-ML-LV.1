import random
import time
import bubble_sort # type: ignore
import insertion_sort # type: ignore
import merge_sort # type: ignore

def timer(funct):
    def wrapper_function(*Args, **Kwargs):
        time0 = time.time()
        funct(*Args, **Kwargs)
        print(f'La función {funct.__name__} demoró {time.time() - time0} en correr')
    return wrapper_function

@timer
def test_small_list(method, list):
    sorted_list = method(list)
    print(f"Sorted list (with {method.__name__}): ")
    print(sorted_list)

def generate_small_list():
    list_size = int(input('Write the desired list size: '))

    list = [random.randint(0,list_size) for i in range(list_size)]
    print("Original List: ")
    print(list)

    return list

@timer
def test_list(method, list):
    sorted_list = method(list)
    print(f"Sorted list (with {method.__name__}): ")

def generate_small_list():
    list_size = int(input('Write the desired list size: '))

    list = [random.randint(0,list_size) for i in range(list_size)]
    print("Original List: ")
    print(list)

    return list

def generate_list(list_size):
    list = [random.randint(0,list_size) for i in range(list_size)]

    return list

def test_method(method):
    list = generate_list()

    test_list(method, list)

    return list

def test_all_methods(list_size):

    list = generate_list(list_size)

    print("- " * 55)
    test_list(bubble_sort.bubble_sort, list)
    print("- " * 25)
    test_list(insertion_sort.insertion_sort, list)
    print("- " * 25)
    test_list(merge_sort.merge_sort, list)
    print("- " * 25)

if __name__ == '__main__':
    list_size = int(input('Write the desired list size: '))

    test_all_methods(list_size)
    test_all_methods(list_size)
    test_all_methods(list_size)
    test_all_methods(list_size)
    test_all_methods(list_size)