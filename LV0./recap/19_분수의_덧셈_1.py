from math import gcd

def solution(numer1, denom1, numer2, denom2):
    
    # 최소공배수(LCM) 계산
    lcm = (denom1 * denom2) // gcd(denom1, denom2)

    # 분자 계산 (두 분수를 같은 분모로 변환 후 더함)
    numer = (numer1 * (lcm // denom1)) + (numer2 * (lcm // denom2))

    # 기약 분수를 만들기 위한 GCD 계산
    gcd_v = gcd(numer, lcm)

    # 기약 분수 반환
    return [numer // gcd_v, lcm // gcd_v]

# 테스트 케이스
print(solution(1, 2, 3, 4))  # [5, 4]
print(solution(9, 2, 1, 3))  # [29, 6]
