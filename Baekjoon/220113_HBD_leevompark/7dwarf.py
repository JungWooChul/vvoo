lst=[int(input()) for i in range(9)]

total=sum(lst)

for i in range(9):
    for j in range(i+1,9):
        if 100==total-(lst[i]+lst[j]):
            num1,num2=lst[i],lst[j]
            lst.remove(num1)
            lst.remove(num2)
            lst.sort()
            
            for i in range(len(lst)):
                print(lst[i])
            break
                
    if len(lst)<9:
        break
