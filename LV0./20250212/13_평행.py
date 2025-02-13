# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

# dots	result
# [[1, 4], [9, 2], [3, 8], [11, 6]]	1
# [[3, 5], [4, 1], [2, 4], [5, 10]]	0 

#첫번째_시도

from itertools import combinations

def solution(dots):

    # 기울기가 같아야 하는거 까지는 알겠음
    # 튜플과 리스트는 뭐가 다를까?
    # mutable vs immutable, hashable, unhashable

    rslt = { (tuple(a), tuple(b)) for a, b in combinations(dots, 2) }

    # print(len(rslt)
    rslt_len_1 = len(rslt)

    rslt_2 = []

    for i,j in rslt:
        rslt_2.append(i[0]-j[0]/i[1]-j[1])

    rslt_len_2 = len(set(rslt_2))

    if rslt_len_1 != rslt_len_2:
        return 1

    return 0

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
