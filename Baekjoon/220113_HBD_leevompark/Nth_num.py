T=int(input())
num_L=[]
for i in range(T):
    lst=list(map(int,input().split()))
    lst.sort(reverse=True)
    num_L.append(lst[2])

for i in range(T):
    print(num_L[i])
    