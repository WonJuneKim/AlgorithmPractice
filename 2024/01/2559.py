import sys
input_sys = sys.stdin.readline
n, k = map(int, input().split())
b = list(map(int, input().split()))
answer = 0
current = 0

# 여기서 n이 100000까지 될 수 있음
for i in range(n-k+1):
    current = sum(b[i:i+k])
    answer = max(current, answer)

print(answer)

