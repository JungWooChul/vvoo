import sys
input=sys.stdin.readline

str=input().rstrip('\n')

for i in str:
    if "a"<=i<="z":
        num=(ord(i)+13)
        if num>ord("z"):
            num=(num%ord("z"))+ord("a")-1
        print(chr(num),end='')
    elif "A"<=i<="Z":
        num=(ord(i)+13)
        if num>ord("Z"):
            num=(num%ord("Z"))+ord("A")-1
        print(chr(num),end='')
    else:
        print(i,end='')
    
    
