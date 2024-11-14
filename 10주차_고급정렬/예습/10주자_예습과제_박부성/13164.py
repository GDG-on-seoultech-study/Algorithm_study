n,k = map(int,input().split())

data = list(map(int,input().split()))

dif = [0] * (len(data) - 1)

for i in range(len(data)-1):
    dif[i] = data[i+1] - data[i]

dif.sort()
total = 0
total = sum(dif[:n-k])
print(total)