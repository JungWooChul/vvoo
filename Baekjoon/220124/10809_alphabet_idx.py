import sys
input=sys.stdin.readline

str=input()
str=str.strip('\n')
alp=[-1 for i in range(26)]

for i in range(len(str)):
    alp_num=ord(str[i])-ord("a")
    if alp[alp_num]==-1:
        alp[alp_num]=i
    
for i in range(len(alp)):
    print(alp[i],end=' ')