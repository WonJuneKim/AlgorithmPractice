from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]
SIZE = 3

def bfs(start):
    q = deque()
    q.append(start)
    graph[start] = 0

    while q:
        now = q.popleft()
        if now == '123456780':
            return graph[now]
        loc = now.find('0')
        nowx, nowy = loc % SIZE, loc // SIZE

        for x, y in zip(dx, dy):
            nx = x + nowx
            ny = y + nowy
            nloc = ny * 3 + nx
            if nx < 0 or nx >= SIZE or ny < 0 or ny >= SIZE:
                continue
            nowList = list(now)
            nowList[loc], nowList[nloc] = nowList[nloc], nowList[loc]
            nxt = ''.join(nowList)
            if not graph.get(nxt):
                graph[nxt] = graph[now] + 1
                q.append(nxt)
    return -1


graph = {}
nowInput = ''
for i in range(SIZE):
    nowInput += ''.join(input().split(' '))
print(bfs(nowInput))