import sys
input=sys.stdin.readline

N=int(input())

def empty_str(a):
    if len(a)==0:
        return 1
    else:
        return 0
    
for _ in range(N):
    lst=[]
    check=0
    str=input()
    str=str.rstrip('\n')
    for j in str:
        if j=='(':
            lst.append(j)
        elif j==')':
            if empty_str(lst)==1:
                check=1
                break;
            else:
                lst.pop()
    if empty_str(lst)!=1:
        check=1
    else:
        pass
    if check==0:
        print("YES")
    else:
        print("NO")
        