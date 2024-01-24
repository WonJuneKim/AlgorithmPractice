from collections import deque

n, m = map(int, input().split())
# graph = []
cheese = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
# for i in range(n):
#     graph.append(list(map(int, input())))
# 좌표 정의
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = []

def bfs():
    time = 0
    queue = deque([[0,0]])
    # queue.append((x,y))
    while True:
        edge = set()
        while queue:
            x,y = queue.popleft()

            if cheese[x][y]==1:
                continue


        # 현재 위치 기준으로 4방향 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            # 공간 이탈 시 pass
                if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
                    continue

                if cheese[x][y] == 0 and cheese[nx][ny]:
                    edge.add((nx,ny))

                if not cheese[nx][ny]:
                    visited[nx][ny] =1
                    queue.append([nx, ny])

            if not len(edge):
                return time

            for i in edge:
                queue.append([i[0],i[1]])
                visited[i[0]][i[1]] = 1
                cheese[i[0]][i[1]] =0

            time += 1
            count.append(len(edge))

print(bfs())
print(count[-1])

