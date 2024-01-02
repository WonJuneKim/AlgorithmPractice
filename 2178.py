from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))




# BFS 코드
def bfs(x,y):
    # 좌표 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))
    #큐가 empty 일때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치 기준으로 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 이탈 시 pass
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            # 못지나가는 경우
            if graph[nx][ny] == 0:
                continue
            # 처음 방문하는 것에 대해서만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    #마지막 최단거리 반환
    return graph[n-1][m-1]

#결과 출력
print(bfs(0, 0))