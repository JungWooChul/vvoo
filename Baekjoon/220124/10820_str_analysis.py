import sys
input=sys.stdin.readline

while True:
    try:
        str=input().rstrip('\n')
        if str=="":
            break  
        analysis_str=[0]*4
    
        for j in str:
            if 'a'<=j<='z':
                analysis_str[0]+=1
            elif 'A'<=j<='Z':
                analysis_str[1]+=1
            elif j.isdigit()==1:
                analysis_str[2]+=1
            elif j==' ':
                analysis_str[3]+=1
                
        print(analysis_str[0],analysis_str[1],analysis_str[2],analysis_str[3])
    except EOFError:
        break
        