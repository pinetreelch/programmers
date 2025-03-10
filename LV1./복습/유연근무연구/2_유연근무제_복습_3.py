def adjust_time(time):
    """출근 희망 시각 + 10분이 60분을 넘어가는 경우 시간 조정"""
    hour = time // 100  # 시
    minute = time % 100  # 분

    minute += 10  # 10분 추가

    if minute >= 60:  # 60분이 넘어가면
        hour += 1  # 시간 증가
        minute -= 60  # 분 조정

    return hour * 100 + minute  # 다시 HHMM 형식으로 변환


def solution(schedules, timelogs, startday):
    answer = 0  # 상품 받을 직원 수

    for i in range(len(schedules)):  # 직원별로 검사
        time_late = adjust_time(schedules[i])  # 10분 추가한 후 올바른 HHMM 변환

        success = True  # 1주일 동안 지각 없이 출근했는지 여부
        day = startday - 1  # 0(월) ~ 6(일)로 맞추기 위해 startday - 1

        for j in range(7):  # 일주일 동안 검사
            if day in [5, 6]:  # 토요일(5), 일요일(6)은 검사 안 함
                day = (day + 1) % 7  # 다음 요일로 이동
                continue

            if timelogs[i][j] > time_late:  # 지각한 경우
                success = False  # 상품 받을 자격 없음

            day = (day + 1) % 7  # 다음 요일로 이동

        if success:  # 지각 없이 출근했으면 상품 받을 수 있음
            answer += 1

    return answer


# 10분을 더했을때 정각이 되는 경우도 생각해야함!!!!
