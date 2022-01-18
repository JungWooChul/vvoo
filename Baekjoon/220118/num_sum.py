num=int(input())
cnt=0
i=1
while num>0:
    num=num-i 
    if num<0:
        break;
    i+=1
    cnt+=1

print(cnt)