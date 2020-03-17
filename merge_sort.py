def merge_sort(collection):
    def merge(left, right):
        result = []
        while left and right:        
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


unsorted = [int(item) for item in input().split()]
print(*merge_sort(unsorted))
