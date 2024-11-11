
n = int(input())
arr= []
for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    tmp = i
    for j in range(n):
        if arr[tmp] < arr[j]:
            arr[tmp], arr[j] = arr[j], arr[tmp]

for num in arr:
    print(num)