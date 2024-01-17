n, k = map(int, input().split())
answer = []
b = list(map(int, input().split()))

for i in range(n-k+1):
    answer.append(sum(b[i:i+k]))

print(max(answer))

