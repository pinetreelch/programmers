#  번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# numer1	denom1	numer2	denom2	result
# 1	           2	  3	       4	[5, 4]
# 9	          2	     1	      3	     [29, 6]

from math import gcd
from math import lcm

def solution(numer1, denom1, numer2, denom2):
    
    #gcd = greatest common dividor 최대공약수
    #lcd = least common multiplier 최대공배수

    lcm_v = lcm(denom1, denom2)

    if denom1 !=lcm_v:
        numer1 *= lcm_v // denom1

    if denom2 !=lcm_v:
            numer2 *= lcm_v // denom2

    return [numer1 + numer2, lcm_v]
        


    return 0

print(solution(1,2,3,4))
