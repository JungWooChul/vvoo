a,b=map(int,input().split())

if a<b:
    tmp=b
    b=a
    a=tmp

for i in range(b):
    if a%(i+1)==0 and b%(i+1)==0:
        GCF=i+1
    
print(GCF,int(a*b/GCF))