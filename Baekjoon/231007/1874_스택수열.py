import sys
input = sys.stdin.readline

N = int(input())
answer_lst = [int(input()) for _ in range(N)]

answer, stack = [], []
check = 0

for i in range(1, N+1):
    # 1부터 N까지의 수를 차례로 돌며 stack에 삽입
    stack.append(i)
    answer.append('+')

    # 반복문을 활용하여 연속적으로 stack pop하는 것을 
    while stack:
        # 스택의 마지막 원소 확인
        if stack[-1]==answer_lst[check]:
            stack.pop(-1)
            answer.append('-')
            check += 1
        else:
            break            
    
if len(stack):
    print('NO')
else:
    for i in answer:
        print(i)
    
