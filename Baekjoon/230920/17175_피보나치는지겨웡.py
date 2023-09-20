import sys
input = sys.stdin.readline

N = int(input())
dp = [1 for _ in range(N+1)]

for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1] + 1 # i-2번째 인덱스의 횟수 + i-1번째 인덱스의 횟수 + 자기 자신

print(dp[-1]%1000000007)

# 2 - f[2] + f[0] + f[1] == 3
# 3 - f[3] + '2' + f[1] == 5
# 4 - f[4] + '3' + '2' == 9
# 5 - f[5] + '3' + '4' == 15
