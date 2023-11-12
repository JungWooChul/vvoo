# 실패한 코드
import sys
input = sys.stdin.readline

bracket = input().strip()

# 레이저를 '_'로 치환
bracket = bracket.replace('()', '_')
stack = []
answer, laser = 0, 0

for elem in bracket:
    if elem == '(':
        stack = list(map(lambda x:x+laser, stack))
        laser = 0 
        stack.append(0)
    elif elem == ')':
        answer += stack.pop()+ laser + 1
    else:
        laser += 1
        
print(answer)
