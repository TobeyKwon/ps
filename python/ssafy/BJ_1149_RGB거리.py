import sys; input = lambda : sys.stdin.readline().rstrip()

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N+1)]
RGB.insert(0, [0] * 3)

# 0 : 빨강 1 : 초록  2: 파랑
for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + RGB[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + RGB[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + RGB[i][2]

print(min(dp[N]))

