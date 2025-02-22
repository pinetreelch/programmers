# 당신은 비밀 조직의 보안 시스템을 뚫고 중요한 정보를 해독해야 합니다.
# 시스템은 1부터 n까지의 서로 다른 정수 5개가 오름차순으로 정렬된 비밀 코드를 가지고 있으며,
# 당신은 이 비밀 코드를 맞혀야 합니다.

# 당신은 비밀 코드를 알아내기 위해 암호 분석 도구를 사용하며,
# m번의 시도를 할 수 있습니다.
# 각 시도마다 서로 다른 5개의 정수를 입력하면,
# 시스템은 그 중 몇 개가 비밀 코드에 포함되어 있는지 알려줍니다.

# 만약 비밀 코드가 [3, 5, 7, 9, 10]이고,
# 입력한 정수가 [1, 2, 3, 4, 5]라면 비밀 코드에 포함된 정수는 3, 5 두 개이므로 시스템은 2를 응답합니다.
# 당신은 m번의 시도 후, 비밀 코드로 가능한 정수 조합의 개수를 알고 싶습니다.

# 비밀 코드에 사용된 정수의 범위가 1~10일 때, 아래와 같이 5번의 시도를 했다고 가정해 보겠습니다.


# 입력한 정수	시스템 응답(일치하는 개수)
# [1, 2, 3, 4, 5]	2개
# [6, 7, 8, 9, 10]	3개
# [3, 7, 8, 9, 10]	4개
# [2, 5, 7, 9, 10]	3개
# [3, 4, 5, 6, 7]	3개

from itertools import combinations


def solution(n, q, ans):
    answer = 0

    random_no = []

    for i in range(1, 11):
        random_no.append(i)

    # 가능한 모든 비밀 코드 조합 중복없이 생성  == > 여기까지는 알겠음
    array = set(combinations(random_no, 5))

    # 각 시도(q)와 시스템 응답(ans)에 대해 가능한 조합 필터링
    for query, match_count in zip(q, ans):
        possible_codes = {
            code
            for code in possible_codes
            if sum(1 for num in query if num in code) == match_count
        }

    # 가능한 비밀 코드의 개수 반환
    return len(possible_codes)

    print(array)

    return answer


print(
    solution(
        10,
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [3, 7, 8, 9, 10],
            [2, 5, 7, 9, 10],
            [3, 4, 5, 6, 7],
        ],
        [2, 3, 4, 3, 3],3
    )
)
