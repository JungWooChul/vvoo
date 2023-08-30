import sys
from collections import deque
input=sys.stdin.readline

N = int(input())
jelly = [[int(j) for j in input().split()]for i in range(N)]

# x,y가 이동할 수 있는 방향의 상대값
dx = [1, 0]
dy = [0, 1]


def bfs(sx, sy):
    queue = deque()
    queue.append([sx,sy])
    
    # 방문 확인을 위한 리스트
    discovered = [[False]*3 for _ in range(N)]
    
    while queue:
        x,y = queue.popleft()
        step = jelly[x][y]
        
        # 끝 지점에 도달했으면 True 반환
        if jelly[x][y] == -1:
            return True
            
        # 좌표에 적혀있는 숫자만큼 이동할 수 있는 모든 경우 파악
        for i in range(2):
            nx, ny = x+dx[i]*step, y+dy[i]*step
            if 0 <= nx < N and 0 <= ny < N:
                if not discovered[nx][ny]:
                    discovered[nx][ny] = True
                    queue.append([nx,ny])

if bfs(0,0):
    print('HaruHaru')
else:
    print('Hing')
