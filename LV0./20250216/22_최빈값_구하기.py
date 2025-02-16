# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.
# 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요.
# 최빈값이 여러 개면 -1을 return 합니다.

from collections import Counter


def solution(array):

    count = Counter(array)
    max_freq = max(count.values())
    modes = [key for key, value in count.items() if value == max_freq]

    return modes[0] if len(modes) == 1 else -1


print(solution([1, 2, 3, 3, 3, 4]))
