n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

def merge_sort(s, e):
    if e - s < 1:
        return
    m = (s + e) // 2
    merge_sort(s, m)
    merge_sort(m + 1, e)
    for i in range(s, e + 1):
        tmp[i] = a[i]
    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            a[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            a[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        a[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        a[k] = tmp[index2]
        k += 1
        index2 += 1

tmp = [0] * n

merge_sort(0, n - 1)

for i in range(n):
    print(a[i])