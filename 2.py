t = int(input())

for i in range (1, t+1):
    p, q, r, s, w = map(int, input().split())

    a_result, b_result = 0, 0
    a_result += w * p
    b_result += q
    if w > r :
        b_result +=(w-r) * s

    print('#%d %d' % (i, min(a_result, b_result)))
