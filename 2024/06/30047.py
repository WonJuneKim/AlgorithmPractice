import sys

input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

n = 1
while True:
  if n % A == 0 and n % B == 0:
    print(n)
    break
  n += 1