import sys
input=sys.stdin.readline
#기억하기!!
N=int(input())
lst=[]

for i in range(N):
    num=int(input())
    lst.append(num)
    
lst.sort()
for i in range(N):
    print(lst[i])