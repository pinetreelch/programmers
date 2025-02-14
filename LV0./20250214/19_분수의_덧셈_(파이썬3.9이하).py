from math import gcd

#파이썬 3.9이하에서는 lcm이 사용불가하다
#from math import lcm #least common multiplier

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    # 최소공배수 구하기
    lcm_v = lcm(denom1, denom2)

    # 공통 분모로 변환한 분자 계산
    new_numer1 = numer1 * (lcm_v // denom1)
    new_numer2 = numer2 * (lcm_v // denom2)

    # 두 분수의 합
    total_numer = new_numer1 + new_numer2

    # 최대공약수로 기약 분수 만들기
    gcd_v = gcd(total_numer, lcm_v)

    return [total_numer // gcd_v, lcm_v // gcd_v]

# 테스트
print(solution(1, 2, 3, 4))  # [5, 4]
