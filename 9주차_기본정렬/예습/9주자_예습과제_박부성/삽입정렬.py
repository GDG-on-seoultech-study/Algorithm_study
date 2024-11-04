#삽입 정렬

n = int(input())
arr= []
for _ in range(n):
    arr.append(int(input()))

for i in range(n - 1):
    tmp = i + 1
    while (tmp > 0):
        if arr[tmp] < arr[tmp - 1]:
            arr[tmp], arr[tmp - 1] = arr[tmp -1], arr[tmp]
        else:
            tmp -= 1
for num in arr:
    print(num)
