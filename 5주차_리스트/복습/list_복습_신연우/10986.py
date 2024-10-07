#배열 / #합배열 / # 3으로 나눈 합 배열 / -> 나머지 같은 애들 찾음
#나머지 똑같은 애들 끼리 합 배열 더한 다음 3으로 나누면 나머지 0
#조합을 통해 최종 경우의 수를 구할 수 있음

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m  #같은 나머지 카운트
answer = 0

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1
    
for i in range(m):
    if C[i] > 1:
        answer += (C[i]*(C[i]-1) // 2)

print(answer)