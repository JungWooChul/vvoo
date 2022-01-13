N = int(input())
lst=list(map(int,input().split()))

def prime_num(x):
    if x==1:
        return 0
    cnt=0
    for i in range(x):
        if x%(i+1)==0:
            cnt+=1
    if cnt==2:
        return 1
    else:
        return 0
    
cnt=0
for i in range(N):
    cnt=cnt+prime_num(lst[i])
    
print(cnt)