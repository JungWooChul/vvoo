import sys
input = sys.stdin.readline

def returnPrime(num_list : list, M : int, N : int):
    # 범위 내의 소수를 저장할 리스트
    primes = []
    for i in range(2, N+1):
        # 남은 수 중에서 가장 작은 수를 소수로 선택
        if num_list[i]:
            # 해당 수의 배수의 prime 여부를 모두 False로 변경
            for j in range(2*i, N+1, i):
                num_list[j] = False
            # M과 N 사이 범위에 포함된 소수만 저장
            if M<=i<=N:
                primes.append(i)
    return primes

M, N = map(int, input().split())

# 소수 판별을 저장할 리스트
# 0,1은 소수X
prime_check = [False, False] + [True] * (N-1)
for prime in returnPrime(prime_check, M, N):
    print(prime)
