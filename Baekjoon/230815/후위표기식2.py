import sys
from string import ascii_uppercase

input=sys.stdin.readline

def calc(op, num1, num2):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    elif op == '/':
        return num1/num2

N = int(input())
str_input = input().rstrip()
num_input = [int(input()) for i in range(N)]

# alp = [i for i in str_input if i.isalpha()]
alp = list(ascii_uppercase)

# 알파벳에 해당하는 수 매핑
alp_num_map = {alp[i] : num for i, num in enumerate(num_input)}
stack = []

for i in str_input:
    # 알파벳(피연산자)은 숫자로 변환하여 stack에 push
    if i.isalpha():
        stack.append(alp_num_map[i])
    # 연산자를 만나면, 연산에 필요한 피연산자 stack에서 pop -> 다시 stack에 push 
    else:
        stack.append(calc(i, stack.pop(-2), stack.pop(-1)))

print('{:.2f}'.format(stack[0]))
