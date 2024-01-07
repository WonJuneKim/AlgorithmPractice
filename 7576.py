import sys
from collections import deque
input = sys.stdin.readline

##토마토의 정보를 입력
m, n = map(int, input().split())
#좌표 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#답
a = 0
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()


# graph = [list(map(int, input().split())) for _ in range(n)]
# queue = deque()

# 위에 코드를 좀 더 원론에 맞게 나눠보았다
# 익은 토마토의 위치인 1을 graph에 추가해준다
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        #익은 토마토 좌표를 가져온다
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 토마토가 사분면 안에 있을 때, 그리고 익지 않은 토마토일때
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

#bfs를 실행
bfs()

for i in graph:
    for j in i:
        # 토마토가 익지 않은 케이스
        if j == 0:
            print(-1)
            exit(0)
    a = max(a, max(i))

# 처음 시작 날짜는 1일이니까 하루빼야함
print(a - 1)