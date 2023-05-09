def solution(park, routes):
    sides = {'E':[0,1], 'W':[0,-1], 'S':[1,0], 'N':[-1,0]}
    row, col = len(park), len(park[0])

    # 로봇의 시작 위치
    start = [[i,j] for i in range(row) for j in range(col) if park[i][j] == 'S']
    start = start[0]
    
    for i in routes:
        step = sides[i.split(' ')[0]] # 방향
        N = int(i.split(' ')[1]) # 칸 수
        step_N = [step[0]*N, step[1]*N]
        
        # 공원을 벗어나는지
        if step[0] == 0 : # 가로 방향 이동
            if start[1] + step_N[1] >= col or start[1] + step_N[1] < 0:
                continue
        else:
            if start[0] + step_N[0] >= col or start[0] + step_N[0] < 0:
                continue
        # 이동 중 장애물이 있는지
        continue_check = 0
        start_tmp = start
        for i in range(N):
            start_tmp = [start_tmp[0]+step[0], start_tmp[1]+step[1]]
            if park[start_tmp[0]][start_tmp[1]] == 'X':
                continue_check += 1
                break
        
        if continue_check == 0:
            start = [start[0]+step_N[0], start[1]+step_N[1]]
            
    return start
