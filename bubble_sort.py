def bubble_sort(array):
  length=len(array)
  for i in range(length-1):
    swapped=False
    for j in range(length-1-i):
      if array[j]>array[j+1]:
        swapped=True
        array[j],array[j+1]=array[j+1],array[j]
    if not swapped:
      break
  return array

array=[int(i) for i in input().split()]
print(*bubble_sort(array))
