sum=0
max=0
for i in range(10):
    p1,p2=map(int,input().split())
    sum=sum-p1
    sum=sum+p2
    if max<sum:
        max=sum
print(max)