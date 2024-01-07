# 성곽
import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

m, n = map(int, input().split())
#좌표 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
M, N = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
# 방향은 8,4,2,1 순서로 남,동,북,서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(a, b, arr, visited, room_num):
    q = deque()
    q.append((a, b))
    visited[a][b] = room_num
    room_size = 1
    while q:
        x, y = q.popleft()
        info = bin(arr[x][y])[2:]  # 15 = 1111(2), '0b' 제거
        info = '0'*(4-len(info))+info   # 4자리로 맞춰주기
        for k, bit in enumerate(info):
            # 벽이 아니면 bfs진행
            if bit == '0':
                nx = x + dx[k]
                ny = y + dy[k]
                if not visited[nx][ny]:
                    visited[nx][ny] = room_num
                    q.append((nx, ny))
                    room_size += 1
            # 벽이면 room_dict에 인접한 방의 정보 추가
            if bit == '1':
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
                    if visited[nx][ny] != room_num:
                        room_dict[visited[nx][ny]].add(room_num)
                        room_dict[room_num].add(visited[nx][ny])
    return room_size


visited = [[0 for _ in range(M)] for _ in range(N)]  # 방문 정보
room_count = 0  # 방의 개수
room_dict = defaultdict(set)    # 인접한 방의 정보
room_info = defaultdict(int)    # 각 방(1~)의 크기
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            room_count += 1
            size = bfs(i, j, arr, visited, room_count)
            room_info[room_count] = size

# room_dict(인접한 방의 정보)를 이용해서 벽 하나 제거시 가장 큰 방의 크기 구하기
break_max = 0
for a in room_dict:
    for b in room_dict[a]:
        break_max = max(break_max, room_info[a]+room_info[b])

# 방의 개수, 가장 큰 방의 크기, 벽 하나 제거시 가장 큰 방의 크기
print(room_count, max(room_info.values()), break_max)