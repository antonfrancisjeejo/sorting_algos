def insertion_sort(array):
    for i in range(1, len(array)):
        insertion_index = i
        while insertion_index > 0 and array[insertion_index - 1] > array[insertion_index]:
            array[insertion_index - 1], array[insertion_index] = array[insertion_index], array[insertion_index - 1]
            insertion_index -= 1
    return array


array = [int(i) for i in input().split()]
print(*insertion_sort(array))
