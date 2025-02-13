# 머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 
# 구슬은 모두 다르게 생겼습니다. 
# 머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, 
# balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요

# balls	share	result
# 3	2	3
# 5	3	10

from itertools import combinations

def solution(balls, share):

    balls_new = range(1,balls+1)
    # balls_new = {combinations(balls_new, share)} #{combinations(..., ...)} → 집합 리터럴로, combinations(...) 객체 한 개만을 원소로 가지는 집합 → 길이 1
    # print(balls_new)
    balls_new = list(combinations(balls_new, share)) # 모든 조합을 실제 튜플로 만들어 담은 리스트 → 길이 = 조합 개수

    return len(balls_new)

print(solution(5, 3)) # 5개중 3개 나누어주는법 

