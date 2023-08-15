import sys
input=sys.stdin.readline

# 입력 받기
N = int(input())
num_lst = [int(input()) for i in range(N)]

# 노드의 순서 : 높이 매핑할 딕셔너리
height_dict = {}

# 루트 노드 먼저 선언
height_dict[num_lst.index(-1)+1] = 0

for idx, num in enumerate(num_lst):
    if num != -1:
				# 부모 노드의 높이 + 1이 해당 노드의 높이
        height_dict[idx+1] = height_dict[num] + 1

# 노드가 들어온 순서대로 각 노드의 높이 출력
for i in sorted(height_dict.items()):
    print(i[1])
