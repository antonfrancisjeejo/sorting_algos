def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        return (
            quick_sort([e for e in data[1:] if e <= data[0]])
            + [data[0]]
            + quick_sort([e for e in data[1:] if e > data[0]])
        )
array=[int(i) for i in input().split()]
print(*quick_sort(array))
