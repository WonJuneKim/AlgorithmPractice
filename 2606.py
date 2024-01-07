cnt=0
def DFS(virus):
    global cnt
    visited[virus]=1

    for i in network[virus]:
        if (visited[i]==0):
            DFS(i)
            cnt+=1

def BFS(virus):
    global cnt
    visited[virus] = 1
    queue = [virus]
    while queue:
        for i in network[queue.pop()]:
            if (visited[i]==0):
                visited[i]=1
                queue.insert(0, i)
                cnt+=1
################MAIN###############
N= int(input())
link = int(input())

network = [[]*(N+1) for _ in range(N+1)]

for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [0]*(N+1)
BFS(1)
#DFS(1)
print(cnt)