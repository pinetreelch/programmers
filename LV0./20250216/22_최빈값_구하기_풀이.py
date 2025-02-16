def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a
    return -1


# 봐야할 풀이 - 딕셔너리 사용
def solution(array):
    answer = 0
    ss = set(array)
    temp = []
    dic = {}
    for s in ss:
        dic[s] = array.count(s)
    data = list(sorted(dic.items(), key=lambda x: -x[1]))
    if len(data) == 1:
        return data[0][0]
    if data[0][1] == data[1][1]:
        return -1
    return data[0][0]
