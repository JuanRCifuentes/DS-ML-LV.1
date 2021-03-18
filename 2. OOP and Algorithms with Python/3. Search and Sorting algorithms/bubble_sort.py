import list_tester # type: ignore

def bubble_sort(list):
    n = len(list)

    for i in range(n):
        for j in range(0, n - i - 1):

            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

if __name__ == '__main__':
    list_tester.test_method(bubble_sort)