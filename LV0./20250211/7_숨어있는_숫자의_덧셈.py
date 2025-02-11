# === 7. 숨어있는 숫자의 덧셈(1) ===

# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# my_string	result
# "aAb1B2cC34oOp"	10
# "1a2b3c4d123"	16

# 첫번째 시도
# 리스트 컴프리헨션(list comprehension)**을 활용하면 더 깔끔하게 만들 수 있다.
def solution(my_string):

    digit_sum = []

    for i in my_string:
        if i.isdigit():
            digit_sum.append(int(i))

    return sum(digit_sum)

print(solution("aAb1B2cC34oOp"))