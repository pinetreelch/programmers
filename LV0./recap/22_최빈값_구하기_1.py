# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.
# 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요.
# 최빈값이 여러 개면 -1을 return 합니다.

def solution(array):

    dic = {}
    
    for i in array:
        if str(i) not in dic:
            dic[str(i)] = 1
        else:
            dic[str(i)] += 1

    # 가장 큰 값 찾기
    max_value = max(dic.values())

    # 가장 큰 값과 해당 키 찾기
    max_key = max(dic, key=dic.get)
    max_value = dic[max_key]

    print(max_key, max_value)  # '3' 3

    return 0

print(solution([1, 2, 3, 3, 3, 3,  4]))