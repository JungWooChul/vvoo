T=int(input())
for i in range(T):
    a,b=map(int,input().split())  #총 데이터의 개수는 항상 a^b개의 형태
    print((a**b)%10)