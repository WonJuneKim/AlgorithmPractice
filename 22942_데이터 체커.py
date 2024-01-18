import sys

N = int(sys.stdin.readline())
circles = []


for i in range(N):
    # 원의 중심 좌표, 반지름을 이용해서 각 원의 원쪽 끝점, 오른쪽 끝점을 저장
    x, r = map(int, sys.stdin.readline().split());
    circles.append((x - r, i))
    circles.append((x + r, i))
#모든 좌표들을 왼쪽 부터 차례로 나열하기 위해 정렬
circles.sort()

stack = []
for c in circles:
    if stack:
        # 기본적인 괄호 문제와 같다
        # 자신이 속한 원(종류별 괄호)을 만나면 pop
        # 현재 원인 c의 번호가 스택의 가장 마지막에 추가된 원의 번호와 같다면 pop 과 같은 말
        if stack[-1][1] == c[1]:
            stack.pop()
        else:
            stack.append(c)
    # 중간에 다른 원의 끝 점이 push, 이 경우 이 전의 점은 pop 될 수 없다
    else:
        stack.append(c)

if stack:
    print('NO')
else:
    print('YES')