import sys

r, c = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 1

def bfs():
    global cnt
    queue = set([(0, 0, graph[0][0])])
    while queue:
        x, y, z = queue.pop()
        cnt = max(cnt, len(z))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이미 사용한 알파벳으로는 갈 수 없기 때문에
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in z:
                queue.add((nx, ny, graph[nx][ny] + z))

bfs()
print(cnt)