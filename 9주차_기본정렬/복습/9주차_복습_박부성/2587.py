arr = []


for _ in range(5):
    arr.append(int(input()))

avg = sum(arr) / 5

for i in range(5):
    for j in range(4):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(int(avg))
print(int(arr[2]))