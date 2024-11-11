import sys

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less, equal, great = [],[],[]
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            great.append(num)
        else:
            equal.append(num)
    return quick(great) + equal + quick(less)

n = sys.stdin.readline()

n_sort = quick(n.strip())

for num in n_sort:
    print(num, end='')
    