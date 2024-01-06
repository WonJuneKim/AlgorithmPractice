import sys
input = sys.stdin.readline

# 상하좌우를 이동하기 위한 좌표
# dr : 행이동, dc : 열이동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


n = int(input())
# arr을 모든 요소가 0인 N 곱하기 N 2차원 배열로 초기화
arr = [[0]*n for _ in range(n)]
## 학생들의 정보를 한번에 받는다, 학생의 번호와 좋아하는 학생들의 번호가 순서대로 저장된다
students = [list(map(int, input().split())) for _ in range(n**2)]

## 학생 수 만큼 for문을 돌며 자리에 앉혀 줌, order은 학생들을 배치하는 순서를 나타내는 변수
for order in range(n**2):
    # student 에는 students 리스트에서 해당 순의 학생 정보가 저장됨
    student = students[order]
    ## 여기다가 가능한 자리를 다 담아서 정렬 후 앉힘, 즉 빈자리를 찾기 위해 tmp 리스트가 사용되는거임
    # tmp 리스트를 좋아하는 학생 수, 빈자리 수, 행 번호, 열 번호 순으로 저장(좋아하는 학생 수가 클수록, 빈 자리수가 클 수록, 행번호, 열번호가 작을수록 앞에 정렬)
    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if arr[nr][nc] in student[1:]:
                            like += 1
                        if arr[nr][nc] == 0:
                            blank += 1
                tmp.append([like, blank, i, j])
    ### !!!! like, blank는 클 수록, 행과 열의 수는 작을수록 답이니 lambda 뒤의 조건을 잘 줘야함!!!
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    ### 정렬 후 젤 앞에 있는 리스트의 행과 열의 번호에 학생 앉히기
    arr[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
## 점수를 매길 때는 학생 순서대로 점수 주기 위해 정렬함
students.sort()

for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] in students[arr[i][j]-1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans-1)
print(result)