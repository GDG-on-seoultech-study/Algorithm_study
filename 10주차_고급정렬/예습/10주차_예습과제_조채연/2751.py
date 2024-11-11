import sys
input = sys.stdin.read

data = input().splitlines()
n = int(data[0])       
arr = list(map(int, data[1:]))  

arr.sort()

sys.stdout.write('\n'.join(map(str, arr)) + '\n')