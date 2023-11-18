import sys
from itertools import combinations
input = sys.stdin.readline

class goldBach(object):
    def __init__(self, nums:list) -> None:
        self.nums = nums
        self.N = max(nums)
        self.RESULT = [] # 결과 저장
        self.primeCheck = [False, False] + [True]*(self.N-1) # 범위 내의 정수에 대해 소수판별을 저장할 리스트 설정
        self.primes = [] # 범위 내의 소수를 저장할 리스트
        pass

    def conjectureOfGoldbach(self):
        # 소수 저장
        self.returnPrime()

        for i in self.nums:
            print(self.primeSum(i))
        return self.RESULT

    def primeSum(self, n:int):
        left, right = 0, len(self.primes) - 1
        while left < right:
            tmp = self.primes[left] + self.primes[right]
            if tmp == n:
                return f"{n} = {self.primes[left]} + {self.primes[right]}"
            if tmp < n:
                left += 1
                continue
            right -= 1
        # 나타낼 수 있는 것이 없으면
        return "Goldbach's conjecture is wrong."

    # 소수 여부 업데이트 및 소수 저장
    def returnPrime(self):
        for i in range(2, self.N+1):
            # 남은 수 중에서 가장 작은 수를 소수로 선택
            if self.primeCheck[i]:
                # 해당 수의 배수의 prime 여부를 모두 False로 변경
                for j in range(2*i, self.N+1, i):
                    self.primeCheck[j] = False
                # 해당 수가 소수이면서 홀수이면 저장
                if i%2 == 1:
                    self.primes.append(i)
        return
                    
num_input = []
while(1):
    N = int(input())
    if N:
        num_input.append(N)
    else:
        break

GB = goldBach(num_input)
GB.conjectureOfGoldbach()
