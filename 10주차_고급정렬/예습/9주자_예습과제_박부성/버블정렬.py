#버블정렬
n = int(input())
arr= []
for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1] , arr[j]
for num in arr:
    print(num)
