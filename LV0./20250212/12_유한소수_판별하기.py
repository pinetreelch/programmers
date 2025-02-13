# 문제 설명
# 소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

# 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
# 두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요. 이 문제

# gcd = greatest common dividor(최대공약수)
# 핵심은 2,5를 제거하는거임
from math import gcd


def solution(a, b):
    # b = b // (a와 b의 최대공약수)
    # b는 b를 (a와 b의 최대공약수)로 나눈 몫
    b //= gcd(a, b) 

    # print('최대공약수 찾기', gcd(a, b)) => 최대공약수는 1
    # print(gcd(a , b))

    # b를 2로 나눴을때 나머지가 0이 될때까지
    while b % 2 == 0:
        b //= 2
        # print(b)
        #몫의 변화
        # 몫 : 10 나머지 : 0
        # 몫 : 5  나머지 : 0
    


    while b % 5 == 0:
        b //= 5
        print(b)
        print(b % 5)
        #몫의 변화
        # 몫 : 1 나머지: 0 왜 나머지가 1로 나오지?

    return 1 if b == 1 else 2

print(solution(7, 20))
