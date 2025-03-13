import itertools

def solution(friends, gifts):

    # 친구들의 이름을 담은 1차원 문자열 배열 friends

    # 주고받은 서물 기록을 담은 1차워 문자열 배열 gifts

    # 두 사람이 선물을 주고받은 기록이 있다면

    # 두 사람이 선물을 주고받을 기록이 없다면 또는 주고받은 수가 같다면
    # 선물지수를 계산해야함(함수로. 선물지수 계산함수)

    # 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return 하도록 solution 함수를 완성해 주세요.

    result = []

    for item in gifts:
        if result[item] is null:
            result[item] = 0





    return ''


print(
    solution(
        ["muzi", "ryan", "frodo", "neo"],
        [
            "muzi frodo",
            "muzi frodo",
            "ryan muzi",
            "ryan muzi",
            "ryan muzi",
            "frodo muzi",
            "frodo ryan",
            "neo muzi",
        ],
    )
)
