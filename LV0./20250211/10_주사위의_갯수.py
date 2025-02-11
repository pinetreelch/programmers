# === 10. 주사위의 갯수 ===
# 머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다. 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때, 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.

# box	n	result
# [1, 1, 1]	1	1
# [10, 8, 6]	3	12

#리팩토링된 코드 - 1 
# multi를 따로 선언하지 않고, reduce()를 사용하면 더 깔끔한 코드 가능!
# Python 3.8 이상에서는 math.prod()를 사용하면 곱셈을 더 직관적으로 처리 가능.
from functools import reduce

def solution(box, n):
    return reduce(lambda x, y: x * y, [m // n for m in box])

print(solution([10, 8, 6], 3))  # 12


#리팩토링된 코드 - 2
# import math

# def solution(box, n):
#     return math.prod(m // n for m in box)

# print(solution([10, 8, 6], 3))  # 12