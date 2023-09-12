import sys
from collections import deque
input=sys.stdin.readline

apple_map = [list(map(int, input().split()))for i in range(5)]
r, c = map(int, input().split()) # r : 행번호, c : 열번호

discovered = [[False for j in range(5)] for i in range(5)]
discovered[r][c] = True  # 해당 x,y 좌표 방문 처리
check = 0
def apple_eating(x, y, apple_map, depth, apple):
    global check
    
    # 3회 이동 이내에 사과 count가 다 채워진 경우
    if apple >= 2:
        check = 1
        return 
    
    # 이동 횟수 초과가 됐는데, 사과 count가 다 채워지지 않을 경우
    if depth >= 3:
        return 

    # 왼쪽
    if y > 0 and discovered[x][y - 1] != True and apple_map[x][y - 1] != -1:
        discovered[x][y-1] = True
        if apple_map[x][y - 1] == 1:
            apple_eating(x, y - 1, apple_map, depth + 1, apple + 1)
        else:
            apple_eating(x, y - 1, apple_map, depth + 1, apple)
        discovered[x][y-1] = False

    # 오른쪽
    if y < 4 and discovered[x][y + 1] != True and apple_map[x][y + 1] != -1:
        discovered[x][y+1] = True
        if apple_map[x][y + 1] == 1:
            apple_eating(x, y + 1, apple_map, depth + 1, apple + 1)
        else:
            apple_eating(x, y + 1, apple_map, depth + 1, apple)
        discovered[x][y+1] = False

    # 위쪽
    if x > 0 and discovered[x - 1][y] != True and apple_map[x - 1][y] != -1:
        discovered[x-1][y] = True
        if apple_map[x - 1][y] == 1:
            apple_eating(x - 1, y, apple_map, depth + 1, apple + 1)
        else:
            apple_eating(x - 1, y, apple_map, depth + 1, apple)
        discovered[x-1][y] = False

    # 아래쪽
    if x < 4 and discovered[x + 1][y] != True and apple_map[x + 1][y] != -1:
        discovered[x+1][y] = True
        if apple_map[x + 1][y] == 1:
            apple_eating(x + 1, y, apple_map, depth + 1, apple + 1)
        else:
            apple_eating(x + 1, y, apple_map, depth + 1, apple)
        discovered[x+1][y] = False


apple_eating(r, c, apple_map, 0, 0)
print(check)
