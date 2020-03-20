def counting_sort(array, place):
    size = len(array)
    count = [0] * 10
    result = [0] * size

    for i in range(size):
        index = array[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] = count[i] + count[i - 1]
    i = size - 1
    while i >= 0:
        index = array[i] // place
        result[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(size):
        array[i] = result[i]


def radix_sort(array):
    max_value = max(array)
    place = 1
    while max_value // place > 0:
        counting_sort(array, place)
        place *= 10
    return array


array = [int(i) for i in input().split()]
print(*radix_sort(array))
