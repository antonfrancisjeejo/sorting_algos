def counting_sort(array):
    length = len(array)
    min_value = min(array)
    max_value = max(array)
    counting_length = max_value + 1 - min_value
    counting_arr = [0] * counting_length

    for item in array:
        counting_arr[item - min_value] += 1
    for i in range(1, counting_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]
    ordered = [0] * length
    for i in range(length-1,-1,-1):
        ordered[counting_arr[array[i] - min_value] - 1] = array[i]
        counting_arr[array[i] - min_value] -= 1
    return ordered


array = [int(i) for i in input().split()]
print(*counting_sort(array))
