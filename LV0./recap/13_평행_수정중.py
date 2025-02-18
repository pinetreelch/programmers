# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

# dots	result
# [[1, 4], [9, 2], [3, 8], [11, 6]]	1
# [[3, 5], [4, 1], [2, 4], [5, 10]]	0 

from itertools import combinations
from collections import Counter

def solution(dots):

    dots = list(combinations(dots, 2))

    slope = []

    for a in dots:
        x1, y1 = a[0]
        x2, y2 = a[1]
        slope.append((x2-x1)/(y2-y1))

    slope_cnt = Counter(slope)

    

    return Counter(slope)

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))