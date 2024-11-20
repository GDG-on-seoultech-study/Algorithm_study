import sys

n, m = map(int, input().split())

A = set(map(int, sys.stdin.readline().split()))

B = set(map(int, sys.stdin.readline().split()))

Ad = A.difference(B)
Bd = B.difference(A)

print(len(Ad) + len(Bd))