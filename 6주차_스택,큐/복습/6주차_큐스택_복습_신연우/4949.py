while True:
    str = input()
    if str == '.':
        break

    stack = []
    dic = {']': '[', ')': '('}
    answer = 'yes'

    for s in str:
        if s == '(' or s == '[':
            stack.append(s)
        elif s in dic:  
            if len(stack) == 0 or stack.pop() != dic[s]:  
                answer = 'no'
                break

    if len(stack) > 0:  
        answer = 'no'

    print(answer)

   
