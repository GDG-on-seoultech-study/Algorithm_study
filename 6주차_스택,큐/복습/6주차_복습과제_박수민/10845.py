# 10845 큐

from collections import deque
import sys
#input = sys.stdin.readline

n = int(sys.stdin.readline())
queue = deque()
inst = "a"

for i in range(n):
    inst = str(sys.stdin.readline().strip())

    if inst == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif inst == 'size':
        print(len(queue))
    elif inst == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif inst == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif inst == 'back':
        try:
            print(queue[len(queue)-1])
        except :
            print(-1)
    elif 'push' in inst:
        a,b = inst.split()
        queue.append(int(b))