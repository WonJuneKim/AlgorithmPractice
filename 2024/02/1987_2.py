def solution(brown, yellow):
    w = (brown / 2) + 1
    h = 1
    # 이게 가로가 더 기니까 가로를 최대로 & 세로를 최소로 해서 맞춰가는 느낌
    while w >= h:
        if (w - 2) * (h - 2) == yellow:
            return [w, h]
        w -= 1
        h += 1


def solution(brown, yellow):
    a = (brown / 2) + 1
    b = 1
    # 이게 가로가 더 기니까 가로를 최대로 & 세로를 최소로 해서 맞춰가는 느낌
    while a >= b:
        #상하 좌우 다 빼
        if (a - 2) * (b - 2) == yellow:
            return [a, b]
        a -= 1
        b += 1


def solution(brown, yellow):
    answer = []
    # 일단 합계를 구한다.
    total = brown + yellow
    for b in range(1, total + 1):
        # 전체를 세로로(세로를 1부터 증가시켜주니까) 나누고, 나누어 떨어지면 total 에서 b를 나눈 값이 a가 된다.
        if (total / b) % 1 == 0:
            a = total / b
            if a >= b:
                if a * 2 + b * 2 == brown + 4:
                    answer = [a, b]

    # answer = [a,b]

    return answer