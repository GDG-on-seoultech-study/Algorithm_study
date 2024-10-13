import sys
n = int(input())

for i in range(n):
    s = sys.stdin.readline().rstrip() # restrip으로 \n없앰
    w = list(s.split())     #공백을 기준으로 문자열 분리해서 리스트 저장
    stack = []
    
    for j in w:
        stack.append(j[::-1])  #뒤집어서 스택에 저장
    
    ans = " ".join(stack)
    print(ans)
  
        