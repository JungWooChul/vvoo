def solution(keymap, targets):
    answer = []
		# targets의 원소 하나씩 검사
    for i in targets:
				# 키 터치 수의 합 저장할 변수
        tmp = 0
				# 문자열의 각 문자들 검사
        for j in i:
						# 해당 문자의 최소 터치 저장할 변수
            min = 100
						# keymap의 원소에서 해당 문자 검사
            for key in keymap:
                if j in key:
                    if min > key.index(j) + 1:
                        min = key.index(j) + 1
						# min이 초기값 100이면 존재하지 않는 key이므로 tmp를 -1로 초기화하고 반복문 탈출
            if min == 100:
                tmp = -1
                break
						# 해당 문자의 터치 수 더하기
            tmp += min
				# 문자열의 총 터치수 저장
        answer.append(tmp)
    return answer
