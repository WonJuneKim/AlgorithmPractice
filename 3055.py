import sys
from collections import deque


r, c = map(int, input().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

#방문 배열을 false 또는 -1로 처리
visited = [[-1] * c for _ in range(r)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque()

for y in range(r):
    for x in range(c):
        # 물은 제일 먼저 이동(queue의 앞에 넣는다)
        if graph[y][x] == '*':
            q.appendleft((y, x))
        # 물을 넣은 후 고슴이를 넣는다
        elif graph[y][x] == 'S':
            q.append((y, x))
            visited[y][x] = 0
        # 출발점에 시간 0 저장
        # 전부 -1로 처리된 상태에서 출발점만 0으로 저장됨


while q:
    y, x = q.popleft()
    cur = graph[y][x]  # 현재 위치를 나타냄
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]  # 다음에 갈 좌표(인접한 가로세로 하나씩)

        # 이 부분 처리가 시간단축이 key가 될수도??
        # 좌표가 graph를 벗어나는 경우
        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            continue
        # 이미 지나친 길은 무시
        if visited[ny][nx] != -1:
            continue
        # 고슴이는 물을 갈 수 없다 + 물은 물이니까 생각할 필요 x
        if graph[ny][nx] == "*":
            continue
        # 돌인 경우
        if graph[ny][nx] == "X":
            continue
        # 물이 비버 한테 가는 경우
        if cur == "*" and graph[ny][nx] == "D":
            continue

        if cur == "S":
            # 도착하는 경우
            if graph[ny][nx] == "D":
                print(visited[y][x] + 1)
                break
            # 그렇지 않을 때는 시간을 기록해준다.
            visited[ny][nx] = visited[y][x] + 1

        graph[ny][nx] = cur  # 고슴이와 물을 번갈아가면서 시행하는 방법 >> 다음 좌표를 고슴<>물 체인지
        q.append((ny, nx))  # 다음 탐색 위치 추가
    else:
        #cur ==s 에서 탈출 못하면 다시 while 문을 반복, 탈출 시 break를 통해 while 문까지 종료
        continue
    break
else:
    #탈출도 실패, while 문도 종료
    print("KAKTUS")