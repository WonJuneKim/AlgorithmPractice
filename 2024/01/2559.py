import sys
input_sys = sys.stdin.readline
n, k = map(int, input().split())
b = list(map(int, input().split()))
#여기에 각 자리까지의 합을 미리 넣어둠
answer = []
answer.append(sum(b[:k]))
#여기에 answer은 단일 값이다.

for i in range(n-k):
    #미리 저장된 구간의 합에 이전꺼를 빼고 다음거를 넣음
    #answer에는 미리 저장된 구간합, b에는 실제 리스트
    answer.append(answer[i] - b[i] + b[k+i])

print(max(answer))