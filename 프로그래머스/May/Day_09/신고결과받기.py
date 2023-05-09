def solution(n):
    answer = 0
    arr = list(range(2,n+1))

    for i in arr:
        tmp = 0
        for j in range(2, int(i**(1/2)) + 1):
            if i%j == 0:
                tmp += 1
                break
        if tmp == 0:
            answer += 1

    return answer
