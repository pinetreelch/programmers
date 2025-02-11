# === 6. 컨트롤 제트 ===
# 숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 
# 문자열에 있는 숫자를 차례대로 더하려고 합니다. 
# 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 
# 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

# s	result
# "1 2 Z 3"	4
# "10 20 30 40"	100
# "10 Z 20 Z 1"	1
# "10 Z 20 Z"	0
# "-1 -2 -3 Z"	-3

# 첫번째 시도
#s[i-1]을 참조하는데, 만약 "Z"가 첫 번째 요소라면 s[i-1]은 IndexError 발생.
#해결 방법: 스택(stack)을 사용하면 자연스럽게 해결됨.
#Z가 나오면 이전 값을 빼는 대신 pop()으로 제거
def solution(s):

    s_sum = 0

    s = s.split(" ")
    for i in range(0, len(s)):
        if s[i] == "Z":
            s_sum -= int(s[i-1])       
        else:
            s_sum += int(s[i])    
    
    return s_sum

print(solution("-1 -2 -3 Z"))

#리팩토링된 코드 
#리스트(LIST)랑 스택(STACK)이랑 다른것인가?

#리스트(list)는 여러 용도로 사용 가능 (임의의 위치 삽입/삭제 가능)
#스택(stack)은 특정한 방식(LIFO)으로만 사용됨 (가장 마지막 요소만 pop() 가능)

# def solution(s):
#     stack = []
    
#     for item in s.split():
#         if item == "Z":
#             if stack:  
#                 # 스택이 비어있지 않다면 pop()
#                 #2까지 들어가있었는데 pop하면 가장 최근에 넣은값이 리스트에서 사라짐
#                 stack.pop() 
#         else:
#             stack.append(int(item))

#     return sum(stack)

# # 테스트
# print(solution("1 2 Z 3"))  # 4
# print(solution("10 20 30 40"))  # 100
