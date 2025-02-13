def solution(n):
    count = 0   # 몇 번째 유효한 수인지 카운팅
    number = 0  # 검사할 자연수 (1부터 올라감)

    while count < n:
        number += 1
        # (1) 3의 배수인 경우 건너뛰기
        # (2) 숫자 '3'이 들어간 경우 건너뛰기
        if (number % 3 == 0) or ('3' in str(number)):
            continue
        
        # 여기까지 왔다면 => 사용 가능한 수
        count += 1

    # count가 n에 도달했을 때의 number가
    # 3x 마을에서 n번째로 사용되는 숫자
    return number

# 테스트
print(solution(15))  # 기대값 25
