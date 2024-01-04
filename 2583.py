import sys
from collections import deque

input = sys.stdin.readline
m, n, k = map(int, input().split())
# 좌표 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
a = []
graph = [[1 for _ in range(n)] for _ in range(m)]


#직사각형
for i in range(k):
    x1, y1, x2, y2 =map(int, input().split())
    for _y in range (y1, y2):
        for _x in range(x1, x2):
            #2차원 리스트에서는 [행][열]로 좌표를 나타낸다.
            graph[_y][_x] = 0



# BFS 코드
def bfs(x,y):
    queue = deque()
    #2178에서는 튜플, 지금은 리스트 사용
    queue.append([x,y])
    graph[y][x] = 0

    count = 1
    #큐가 empty 일때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치 기준으로 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 이탈 시 pass
            if 0 <= nx < n and 0 <=ny < m:
                if graph[ny][nx] ==1:
                    graph[ny][nx] =0
                    queue.append([nx, ny])
                    count += 1
    a.append(count)

for _x in range(n):
    for _y in range(m):
        # 못지나가는 경우
        if graph[_y][_x] == 1:
            bfs(_x, _y)

a.sort()
print(len(a))
for count in a:
    print(count, end=' ')