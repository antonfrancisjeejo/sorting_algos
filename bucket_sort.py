DEFAULT_BUCKET_SIZE = 5


def bucket_sort(array, bucket_size=DEFAULT_BUCKET_SIZE):
    min_value, max_value = min(array), max(array)
    buckets_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for i in range(buckets_count)]

    for i in range(len(array)):
        buckets[int((array[i] - min_value) // bucket_size)].append(array[i])
    return sorted(buckets[i][j] for i in range(len(buckets)) for j in range(len(buckets[i])))


array = [int(i) for i in input().split()]
print(*bucket_sort(array))
