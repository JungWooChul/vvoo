N=int(input())
lst=list(map(int,input().split()))
lst.sort()

if N%2==0:
    print(lst[0]*lst[N-1])
else:
    N=int(N/2)
    print(lst[N]**2)