import sys
input=sys.stdin.readline

N=int(input())
lst=[]

for i in range(N):
    st=input()
    st=st.strip('\n')
    split_st=st.split(' ')
    
    if split_st[0]=='push':
        lst.append(split_st[1])
    elif split_st[0]=='pop':
        if len(lst)==0:
            print(-1)
        else:
            print(lst.pop(len(lst)-1))
    elif split_st[0]=='size':
        print(len(lst))
    elif split_st[0]=='empty':
        if len(lst)==0:
            print(1)
        else:
            print(0)
    elif split_st[0]=='top':
        if len(lst)==0:
            print(-1)
        else:
            print(lst[len(lst)-1])
        