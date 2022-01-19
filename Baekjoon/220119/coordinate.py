N=int(input())
lst=[]

lst=[list(map(int,input().split())) for _ in range(N)]

lst.sort(key=lambda x:(x[0],x[1]))

for x,y in lst:
    print(x,y)