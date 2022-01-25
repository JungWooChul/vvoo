import sys
input=sys.stdin.readline

str=input().rstrip('\n')
len_str=len(str)
lst=[]

for i in range(len_str):
    lst.append(str)
    str=str[1:len_str+1-i]
    
lst.sort()
for j in lst:
    print(j)
