input = __import__('sys').stdin.readline
import math

def find_fives(n):
    t = 5
    cnt = 0
    while t <= n:
        cnt += n // t
        t *= 5
    return cnt
n = int(input())

for i in range(n):
    t = int(input())
    print(find_fives(t))