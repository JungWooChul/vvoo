import sys
input = sys.stdin.readline

N = int(input())
num_stack = []

for _ in range(N):
    command = input().strip().split()
    if command[0] == 'push':
        num_stack.append(command[1])
    
    elif command[0] == 'pop':
        try:
            tmp = num_stack.pop()
            print(tmp)
        except:
            print(-1)
    
    elif command[0] == 'size':
        print(len(num_stack))

    elif command[0] == 'empty':
        print(1 if len(num_stack)==0 else 0)

    elif command[0] == 'top':
        try:
            print(num_stack[-1])
        except:
            print(-1)
