import sys
input=sys.stdin.readline
num=int(input())
Q=[]

def empty_Q(lst):
    if len(lst)==0:
        return 1
    else:
        return 0
    
for _ in range(num):
    str=input()
    str=str.strip('\n')
    split_str=str.split(' ')
    
    if split_str[0]=='push':
        Q.append(split_str[1])
    elif split_str[0]=='pop':
        if empty_Q(Q)==1:
            print(-1)
        else:
            print(Q.pop(0))
    elif split_str[0]=='size':
        print(len(Q))
    elif split_str[0]=='empty':
        if empty_Q(Q)==1:
            print(1)
        else:
            print(0)
    elif split_str[0]=='front':
        if empty_Q(Q)==1:
            print(-1)
        else:
            print(Q[0])
    elif split_str[0]=='back':
        if empty_Q(Q)==1:
            print(-1)
        else:
            print(Q[len(Q)-1])
            