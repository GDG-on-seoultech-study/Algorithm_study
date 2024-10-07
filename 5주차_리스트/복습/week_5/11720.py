"""
    Descr:  자료구조 스터디, list & array
"""

# 11720 숫자의 합
n = int(input())
num = input()
total = 0
for i in range(n):
    total += int(num[i])

print(total)
