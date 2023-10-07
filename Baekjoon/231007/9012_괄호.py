import sys
input = sys.stdin.readline

def check_vps(vps):
    open_pare = '('
    stack = []
    for pare in is_vps:
        if pare == open_pare:
            stack.append(pare)
        else:
			# 2. stack.pop()에서 오류발생 -> 괄호의 짝이 맞지 않음을 의미
            try:
                check = stack.pop()
				# 1. pop한 원소와 짝이 맞지 않는 경우
                if check != open_pare:
                    return 'NO'
            except:
                return 'NO'

    # 3. stack에 원소가 남아있는지 판단
    return 'YES' if len(stack)==0 else 'NO'
                
N = int(input())
for i in range(N):
    is_vps = input().strip()
    print(check_vps(is_vps))
