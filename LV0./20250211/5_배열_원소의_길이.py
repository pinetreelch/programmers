# === 5. 배열 원소의 길이 ===

# 문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 return하도록 solution 함수를 완성해주세요.

# ["We", "are", "the", "world!"]	[2, 3, 3, 6]
# ["I", "Love", "Programmers."]	[1, 4, 12]


def solution(strlist):
    return list( len(i) for i in strlist)
    #  return list(map(len, strlist)) #! len도 사용이 가능한 상황인듯

print(solution(["We", "are", "the", "world!"]))