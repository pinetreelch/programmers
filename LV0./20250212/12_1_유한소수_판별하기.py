def solution(a, b):
    answer = 0

    #기약분수로 만들기
    for i in range(2, min([a, b]) + 1):
        while a % i == 0 and b % i == 0:
            a = a // i
            b = b // i

    #분모에서 2제거
    while b % 2 == 0:
        b = b // 2

    #분모에서 5제거
    while b % 5 == 0:
        b = b // 5

    #2랑 5를 제거했을때 몫이 1만 남았으면 유한소수
    if b == 1:
        answer = 1
    #1, 2, 5를 제외한 어떤 숫자가 있으면 무한소수임
    else:
        answer = 2
    return answer
