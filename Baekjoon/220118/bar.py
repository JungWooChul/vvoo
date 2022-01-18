X=int(input())
cnt=0

lst=[64,32,16,8,4,2,1]

for i in range(len(lst)):
    if X>=lst[i]:
        if X-lst[i]>=0:
            X=X-lst[i]
            cnt+=1
            if X==0:
                print(cnt)
                break;
    
    

