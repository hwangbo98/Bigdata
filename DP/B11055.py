import sys 

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

dp = A[:]
# dp[0] = A[0]
for i in range(N) :
    for j in range(i) :
        if A[i] > A[j] :
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))