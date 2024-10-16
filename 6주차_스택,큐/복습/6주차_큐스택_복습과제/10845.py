from collections import deque
import sys
dq = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        dq.append(cmd[1])
    elif cmd[0] == 'pop':

        if dq:
            print(dq.popleft())
        elif not dq:
            print(-1)
            
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':

        if not dq:
            print(1)
        elif dq:
            print(0)
    elif cmd[0] == 'front':

        if dq:
            print(dq[0])
        else:print(-1)
    elif cmd[0] == 'back':
        if dq:
            print(dq[-1])
        else:print(-1)