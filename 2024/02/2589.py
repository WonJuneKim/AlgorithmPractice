import sys;
from collections import deque


def bfs(N, M, r, c):
    Q.append((r, c))
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    sums = 0
    while Q:
        r, c = Q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] == 'L' and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    sums = max(sums, visited[nr][nc])
                    Q.append((nr, nc))
    return sums - 1


N, M = map(int, sys.stdin.readline().split())

maps = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

Q = deque()
visited = [[0] * M for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'L' and visited[i][j] == 0:
            if 0 <= i - 1 < N and 0 <= i + 1 < N:
                if maps[i - 1][j] == 'L' and maps[i + 1][j] == 'L':
                    continue
            if 0 <= j - 1 < M and 0 <= j + 1 < M:
                if maps[i][j - 1] == 'L' and maps[i][j + 1] == 'L':
                    continue
            result = max(result, bfs(N, M, i, j))

print(result)