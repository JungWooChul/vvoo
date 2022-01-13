T=int(input())

def factorial(x):
    sum=1
    for i in range(x):
        sum*=(i+1)
        
    return sum

for i in range(T):
    n,m=map(int,input().split())
    print(int(factorial(m)/(factorial(n))))
    

            
