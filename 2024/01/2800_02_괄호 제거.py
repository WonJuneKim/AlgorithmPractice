from itertools import combinations

expr = list(input())
indices = [] # 괄호의 시작과 끝 인덱스를 저장하는 리스트
stack = [] # 여는 괄호의 index를 저장
answers = set() # 중복된 문자열을 피하기 위해 set를 사용

# 괄호 쌍의 index를 찾는다
for i in range(len(expr)):
    if expr[i] == '(':
        stack.append(i)
    elif expr[i] == ')': # 찾은 괄호 쌍의 괄호를 제거한 모든 경우의 수를 찾는다.
        indices.append((stack.pop(), i))

# 괄호 쌍을 조합하여 제거한 모든 경우의 수 찾기
for i in range(len(indices)): # 가능한 괄호 쌍의 개수에 대해 반복
    for comb in combinations(indices, i+1): # 현재 개수 i+1 개 만큼의 괄호 쌍에 대해 모든 조합을 생성
        temp = expr[:] # 원본 문자열을 복사하여 temp에 저장
        for idx in comb: # 조합된 괄호쌍을 제거
            temp[idx[0]] = temp[idx[1]] = ""
        answers.add("".join(temp)) # 제거된 괄호를 가진 문자열을 결과에 추가

# 정렬된 순서로 결과 출력
for item in sorted(list(answers)):
    print(item)