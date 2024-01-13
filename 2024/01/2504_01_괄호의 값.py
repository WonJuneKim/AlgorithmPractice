import sys
def input():
    return sys.stdin.readline().rstrip()

s = input()
stack = []

# 괄호열을 입력받는 것
# 조건을 충족하는 경우 stack에 넣는다, 그 외의 경우는 스택에 넣지 않음
for test in s:
    # 여는 괄호는 어떤 경우에도 합당
    if test == '(':
        stack.append('(')
    elif test == '[':
        stack.append('[')
    elif test == ')':
        # 닫는 괄호는 스택이 비어있지 않고, 스택의 맨 위가 여는 괄호 일 때 스택 맨 위에서 여는 괄호를 제거 후 진행
        # 여는 괄호 둘을 기준점으로 삼는것
        # 닫는 괄호는 따로 저장을 하지 않음
        if stack and stack[-1] == '(':
            stack.pop(-1)
        else:
            print(0)
            exit(0)
    else:
        # 이전 case와 같은 원리
        if stack and stack[-1] == '[':
            stack.pop(-1)
        else:
            print(0)
            exit(0)

# 위의 조건들로 문자열을 모두 처리한 후에는 여는 괄호가 모두 stack에서 제거 되어야한다.
# stack에 남아 있는 경우는 올바르지 않은 문자열이다.
if stack:
    print(0)
    exit(0)


# 식으로 표현된 부분을 숫자로 계산하는 부분
def compress():
    # Integer를 하나로 합쳐야 하니깐 길이가 2 이상이어야 함.
    # stack의 길이가 1보다 클 때까지 반복한다.
    while len(stack) > 1:
        # 두 개의 값이 무조건 Integer이어야 하므로
        # Integer면 첫번째 원소가 None으로 되어 있음
        a, integer1 = stack[-1] # stack[-1]은 스택의 맨 위의 값을 가져오는 것, 맨 위의 값 중 첫번째는 a에 두번째는 integer1에 저장
        b, integer2 = stack[-2]
        # 두 항목 중 하나라도 none이면 종료(이미 계산이 완료되었음)
        if a or b:
            break
        # 두 항목은 계산이 완료되었으므로 stack에서 제거
        stack.pop()
        stack.pop()
        # 계산된 값을 다시 stack에 추가
        stack.append((None, integer1 + integer2))

for test in s:
    #compress로 지정한 함수를 사용하기 위해 여는 괄호를 만나면 해당 괄호는 스택에 추가, 대응하는 정수 값(2,3)도 추가
    if test == '(':
        stack.append(('(', 2))
    elif test == '[':
        stack.append(('[', 3))
    elif test == ')' or test == ']': # 스택의 길이는 항상 1이상일때를 상정
        last1, last2 = stack.pop()
        # 상위 항목이 None이 아닌경우, 해당 항목의 정수값을 그대로 스택에 추가
        if last1 != None:
            stack.append((None, last2))
        # 상위 항목이 None 인 경우, 두번째 상위 항목을 가져와서 항목의 정수값을 곱한 값을 스택에 추가
        else:
            a, b = stack.pop()
            stack.append((None, last2 * b))
        # 닫는 괄호를 처리할 때 마다 compress 함수를 실행(스택을 압축하는 역할)
        compress()

# stack의 최상위 항목에 잇는 정수 값을 출력한다.
print(stack[-1][1])