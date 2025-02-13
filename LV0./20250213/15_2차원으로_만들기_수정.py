def solution(num_list, n):
    # 방법 1) 리스트 슬라이싱 + for range
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer

# 또는, 간단히 리스트 컴프리헨션을 사용할 수도 있습니다.
def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]

# 테스트
print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
# [[1, 2], [3, 4], [5, 6], [7, 8]]
