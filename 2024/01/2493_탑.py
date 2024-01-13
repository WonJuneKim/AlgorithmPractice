import sys
input = sys.stdin.readline
n = int(input())
tops = list(map(int,input().split()))
answer = [0] * n
stack = []

# 본인과 높이가 같거나 그 이상일 경우 신호를 수신한다.
for i in range(len(tops)):
    while stack:
        # 스택의 특성상 현재의 탑이 맨 위에 있는 탑보다 높은지 확인
        # 이 경우 해당 탑은 신호를 받을 수 없음
        if tops[stack[-1][0]]<tops[i]:
            stack.pop()
        # 스택 맨 위의 탑이 현재 탑에서 신호를 받을 수 있음
        # 따라서 스택의 맨 위의 탑의 index에 1를 더하여 설정
        # 이후 다시 탐색, 결과는 answer에 저장(갱신)되어서 가장 가까운 높은 탑의 index를 나타냄
        else:
            answer[i] = stack[-1][0]+1
            break
    stack.append((i,tops[i]))
print(*answer)