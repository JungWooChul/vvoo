p,q=map(int,input().split())
check=0
for i in range(p):
    if p%(i+1)==0:
        check+=1
        if check==q:
            print(i+1)
            break;
if check<q:
    print(0)