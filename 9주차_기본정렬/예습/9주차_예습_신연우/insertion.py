n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

for i in range(1, n):
    s = a[i]
    for j in range(i-1, -1, -1):
        if a[j] > s:
            a[j +1] = a[j]
        else:
            a[j + 1] = s
            break
    else:
        a[0] = s

for i in range(len(a)):
    print(a[i])