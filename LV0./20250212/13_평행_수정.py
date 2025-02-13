from itertools import combinations

def solution(dots):
    slopes = []

    # dots에서 2개씩 뽑아 모든 '선'을 구한다.
    for (x1, y1), (x2, y2) in combinations(dots, 2):
        # 수직선(기울기 = 무한대) 처리
        
        if x1 == x2:  
            # float('inf') 는 파이썬에서 양의 무한대(positive infinity)를 의미하는 부동소수점 값입니다.
            slope = float('inf')
        else:
            slope = (y2 - y1) / (x2 - x1)
        
        slopes.append(slope)
    
    # slopes에 들어간 기울기 개수와 set으로 만든 후의 개수를 비교
    # => 중복 기울기가 있으면 평행선 존재
    if len(slopes) != len(set(slopes)):
        return 1
    else:
        return 0

# 테스트
print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))  # 예시: 1
