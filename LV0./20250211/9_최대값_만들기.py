# === 9. 최대값 만들기 ===

# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# numbers	result
# [1, 2, 3, 4, 5]	20
# [0, 31, 24, 10, 1, 9]	744


#시도2 - 모든 조합을 통해서 가장 큰것 찾기 #!중요하다고 생각함
from itertools import combinations

def solution(numbers):
    # 모든 두 개의 조합을 생성하여 곱한 값들을 set에 저장
    products = {a * b for a, b in combinations(numbers, 2)}
    return max(products)  # 최댓값 반환

# 테스트
print(solution([1, 2, 3, 4]))  # 12