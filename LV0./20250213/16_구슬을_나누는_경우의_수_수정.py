# 만약 “5개 중 3개를 고르는 방법의 수가 몇 개인지(=조합의 개수)”만 알고 싶다면, 파이썬 3.8+에서 제공하는 math.comb 함수를 사용할 수 있습니다
# 조합의 갯수 = 이항갯수
from math import comb

def solution(balls, share):
    return comb(balls, share)

print(solution(5, 3))
