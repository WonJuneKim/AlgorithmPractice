import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dictionary = {}

for i in range(1, n+1):
    a = input().rstrip()
    dictionary[i] = a
    dictionary[a] = i


for i in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(dictionary[int(a)])
    else:
        print(dictionary[a])