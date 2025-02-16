def solution(n):
    return (n - 1) // 7 + 1


def solution(n):
    return -(-n // 7)


def solution(n):
    answer = 0

    if n % 7 != 0:
        answer = (n // 7) + 1
    else:
        answer = n // 7

    return answer
