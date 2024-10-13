n = int(input())

stack = []

for i in range(n):
    a = input()
    
    for j in a:
        if j == '(':
            stack.append('(')
        elif j == ")":
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()
    
    if len(stack) != 0:
        print("No")
    else: 
        print("YES")
     
