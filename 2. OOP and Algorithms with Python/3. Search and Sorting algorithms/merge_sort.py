import list_tester # type: ignore

def merge_sort(list):
    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]

        merge_sort(left)
        merge_sort(right)

        right_index = 0
        left_index = 0
        list_index = 0

        while right_index < len(right) and left_index < len(left):
            if left[left_index] < right[right_index]:
                list[list_index] = left[left_index]
                left_index += 1
            else:
                list[list_index] = right[right_index]
                right_index += 1

            list_index += 1
        
        while left_index < len(left):
            list[list_index] = left[left_index]
            left_index += 1
            list_index += 1
        
        while right_index < len(right):
            list[list_index] = right[right_index]
            right_index += 1
            list_index += 1
        
        return list

if __name__ == '__main__':
    list_tester.test_method(merge_sort)