def selection_sort(array):
    length = len(array)
    for i in range(length):
        least = i
        for j in range(i + 1, length):
            if array[j] < array[least]:
                least = j
        if least != i:
            array[i], array[least] = array[least], array[i]
    return array


array = [int(i) for i in input().split()]
print(*selection_sort(array))
