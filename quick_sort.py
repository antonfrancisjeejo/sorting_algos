def quick_sort(array):
  length=len(array)
  if length<=1:
    return array
  else:
    pivot=array.pop(0)
    greater,lesser=[],[]
    for item in array:
      if item<pivot:
        lesser.append(item)
      else:
        greater.append(item)
    return quick_sort(lesser)+[pivot]+quick_sort(greater)


array=[int(i) for i in input().split()]
print(*quick_sort(array))
