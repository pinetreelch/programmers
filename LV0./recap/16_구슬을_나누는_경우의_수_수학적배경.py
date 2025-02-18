#배열
# 조합(combination)이란 순서를 고려하지 않고 주어진 개수에서 일부를 선택하는 방법의 개수를 의미한다.
# 조합 공식:
# C(n,r)= n! / r!(n−r)! 

from math import factorial

def solution(balls, share):
    return factorial(balls) // (factorial(share) * factorial(balls - share))

print(solution(5, 3))