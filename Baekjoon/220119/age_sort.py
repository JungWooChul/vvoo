import sys
input=sys.stdin.readline

N=int(input())

lst=[list(map(str,input().split())) for _ in range(N)]

lst.sort(key=lambda x:int(x[0]))
for x,y in lst:
    print(x,y)