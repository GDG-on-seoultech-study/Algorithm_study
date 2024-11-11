import sys

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num == pivot:
            equal_arr.append(num)
        else:
            greater_arr.append(num)
    return quick(greater_arr) + equal_arr + quick(lesser_arr)

n, k = map(int, input().split())

score = list(map(int, input().split()))

sort_arr = quick(score)

print(sort_arr[k-1])