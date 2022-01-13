A,B=map(int,input().split())

def _EZ(a,b):
    lst=[]
    for i in range(b):
        for j in range(i+1):
            lst.append(i+1)
    
    sum=0
    for i in range(a-1,b):
        sum=sum+lst[i]
    return sum

print(_EZ(A,B))
    