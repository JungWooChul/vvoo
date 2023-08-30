import sys
from collections import defaultdict

def DFS(edge_dict, v, discovered=[]):
    discovered.append(v)
    for i in edge_dict[v]:
        if not i in discovered:
            discovered = DFS(edge_dict, i, discovered)
    
    return discovered

def BFS(edge_dict, v):
    discovered = [v]
    queue = [v]
    while queue:
        v = queue.pop(0)
        for i in edge_dict[v]:
            if i not in discovered:
                discovered.append(i)
                queue.append(i)
    return discovered

input=sys.stdin.readline
edge_dict = defaultdict(list)   # 그래프를 딕셔너리 자료형으로 표현

N, M, V = map(int, input().split())

for i in range(M):
    node1, node2 = map(int, input().split())
    edge_dict[node1].append(node2)
    edge_dict[node2].append(node1)

# 딕셔너리 value 값 정렬
for key in edge_dict.keys():
    edge_dict[key].sort()

print(*DFS(edge_dict, V))
print(*BFS(edge_dict, V))
