from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

#방문 배열을 false 또는 -1로 처리
visited = [[False] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


# 섬의 개수를 구하고 섬마다 번호를 표시하는 bfs
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    graph[x][y] = mark

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = mark
                    visited[nx][ny] = True


# 섬 사이 최단거리를 구하는 bfs
def bfs2(island):
    q = deque()
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == island:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != island and graph[nx][ny] != 0:  # 다른 섬과 만났을 경우
                    return dist[x][y]
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:  # 물이고 아직 건너지 않은 곳일 경우
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))


mark = 1  # 섬마다 번호를 체크하기 위한 값
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and not visited[x][y]:
            island_cnt = bfs(x, y)
            mark += 1

result = sys.maxsize  # 최솟값을 구하기 위해 가장 큰 값으로 세팅
for island in range(1, mark):
    result = min(result, bfs2(island))

print(result)