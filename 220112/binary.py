num=int(input())
for i in range(num):
    case=int(input())
    bin_case=int(format(case,'b'))
    check=0
    while bin_case!=0:
        if bin_case%10==1:
            print(check,end=' ')
        bin_case=int(bin_case/10)
        check+=1