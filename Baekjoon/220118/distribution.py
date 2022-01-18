T=int(input())
nums=[]
for i in range(T):
    a,b=map(int,input().split())
    b=int(b%4)
    if b==0:
        b=4
    num=1
    for j in range(b):
        num=num*a 
        num=int(num%10)
    if num==0:
        num=10
    nums.append(num)
    
for i in range(T):
    print(nums[i])
    