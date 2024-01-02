t = int(input())  # 테스트 케이스의 수 입력
results = []
for test_case in range(1, t + 1):
    num = list(map(int, input().split()))
    sum=0
    for i in num:
        if i %2 ==1:
            sum += i
    print('#'+str(test_case), str(sum))
