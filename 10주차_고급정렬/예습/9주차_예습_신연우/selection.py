n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

for i in range(len(a)):
    min = i
    for j in range(i+1, len(a)):
        if a[min] > a[j]:
            min = j
    if a[i] > a[min]:
        temp = a[i]
        a[i] = a[min]
        a[min] = temp

for i in range(len(a)):
    print(a[i])