# 3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.#

# 10진법 3x 마을에서 쓰는 숫자	10진법	3x 마을에서 쓰는 숫자
# 1	1	6	8
# 2	2	7	10
# 3	4	8	11
# 4	5	9	14
# 5	7	10	16

# n	result
# 15	25
# 40	76

def solution(n):

    cnt = 1
    rslt = 1

    while cnt < n:

        rslt += 1

        if rslt % 3 == 0:
            continue
        elif '3' in str(rslt):
            continue
        
        cnt += 1
        
        
    print(rslt)
    
    return 0

print(solution(15))