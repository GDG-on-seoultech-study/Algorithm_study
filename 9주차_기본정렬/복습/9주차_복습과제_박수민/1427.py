import sys

input = sys.stdin.readline

num = input().strip("\n")
n = len(num)
a = []


for i in str(num):
    a.append(int(i))

#bubble
for i in range(n):
    ind = i
    for j in range(n):
        if a[ind] > a[j]:
            a[ind], a[j] = a[j], a[ind]
#a.sort(reverse=True) #내림차순 sort. bubble 대신 사용가능

for i in a:
    print(i, end="")

