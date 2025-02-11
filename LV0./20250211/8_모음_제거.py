# === 8. 모음 제거===
# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# my_string	result
# "bus"	"bs"
# "nice to meet you"	"nc t mt y"

#첫번째 시도
#리스트 컴프리헨션이나 filter()를 사용하면 더 깔끔한 코드 가능.
def solution(my_string):

    #한개라도 포함되는지 확인하는 any()함수
    # if any(vowel in "bus" for vowel in ["a", "e", "i", "o", "u"]):
    #     print("Yes")
    # else:
    #     print("No")

    for character in ["a", "e", "i", "o", "u"]:
        if character in my_string:
            my_string = my_string.replace(character, " ")

    return my_string

print(solution("bus"))

#리펙토링된 코드 -2
# def solution(my_string):
#     return "".join([char for char in my_string if char not in "aeiou"])

# print(solution("bus"))  # "bs"