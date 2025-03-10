def solution(schedules, timelogs, startday):
    
    # 시간 +10분을 처리하는 함수
    def add_late_margin(time):

        hour = time // 100
        minute = time % 100 + 10

        if minute >= 60:
            hour += 1
            minute -= 60

        return hour * 100 + minute

    result = 0  # 출석 인정 인원 수

    for idx, desired_time in enumerate(schedules):
        deadline = add_late_margin(desired_time)  # 지각 기준 시각
        day = startday  # 시작 요일
        is_late = False

        for time_log in timelogs[idx]:
            if day in (6, 7):  # 주말은 제외
                day = (day % 7) + 1  # 요일 순환 처리
                continue

            if time_log > deadline:  # 지각한 경우
                is_late = True
                break

            day = (day % 7) + 1  # 요일 순환 처리

        if not is_late:
            result += 1  # 지각이 없으면 결과에 추가

    return result


print(
    solution(
        [730, 855, 700, 720],  # 직원들 n 명이 설정한 출근 희망 시각
        [
            # 직원들이 일주일 동안 출근한 시각
           [710, 700, 650, 735, 700, 931, 912], 
           [908, 901, 805, 815, 800, 831, 835], 
           [705, 701, 702, 705, 710, 710, 711], 
           [707, 731, 859, 913, 934, 931, 905]
        ],
        1,
    )
)

