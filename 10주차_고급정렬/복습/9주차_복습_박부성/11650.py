import sys

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    great, equal, less = [], [], []
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            great.append(num)
        else:
            equal.append(num)
    return quick(less) + equal + quick(great)



n = int(input())
xy = [[] for _ in range(n)]
for i in range(n):
    xy[i] = list(map(int, sys.stdin.readline().split()))

xy_sort = quick(xy)

for i in range(n):
    print(*xy_sort[i])