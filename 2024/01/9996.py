import sys

n = int(input())
pattern = input().split("*")
k = len(pattern[0]) + len(pattern[1])

for _ in range(n):
    word = input()

    if len(word) >= k and word.startswith(pattern[0]) and word.endswith(pattern[1]):
        print("DA")
    else:
        print("NE")