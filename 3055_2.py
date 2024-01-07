import sys
from collections import deque
input = sys.stdin.readline

# 좌표입력
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input().rstrip()))
visited = [[False] * C for _ in range(R)]

queue = deque()

for i in range(R):
    for j in range(C):
        if graph[i][j] == "D":
            goal = [i, j]
            graph[i][j] = sys.maxsize
        elif graph[i][j] == "S":
            start = [i, j, 0]
            graph[i][j] = "."
        elif graph[i][j] == "*":
            graph[i][j] = 0
            queue.append([i, j, 0])
        elif graph[i][j] == "X":
            visited[i][j] = True

# 물 차는 시간 UPDATE
while queue:
    x, y, cnt = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == ".":
            graph[nx][ny] = cnt + 1
            queue.append([nx, ny, cnt + 1])

# 고슴도치 이동
queue.append(start)
flag = False
visited[start[0]][start[1]] = True
while queue:
    x, y, cnt = queue.popleft()
    if [x, y] == goal:
        flag = True
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
            if graph[nx][ny] == "." or graph[nx][ny] > cnt + 1:
                visited[nx][ny] = True
                queue.append([nx, ny, cnt + 1])

if flag:
    print(cnt)
else:
    print("KAKTUS")

# arr에 비버의 굴(D)는 sys.maxsize로 update한다.
# 고슴도치는 이동하므로 고슴도치(S)의 위치를 start에 저장하고 비어있는 곳(.)으로 바꾸어준다.
# 물은 차는 시간으로 바꾸어 주기 위해 시작은 0으로 바꾸어준다.
# X는 돌이므로 고슴도치가 방문하지 못하게 visited 배열을 True로 바꾸어준다.
# 물을 퍼지게 하는 BFS를 한다. 비어있는 곳(.) 에만 퍼지게 하고 채워지는 시간으로 채워진다.
# 고슴도치는 비어있는곳(.) 또는 물이 찰 시간을 보고 물이 차지 않았다면 이동한다.